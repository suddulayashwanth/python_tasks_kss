import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "students.db"))
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class StudentDB(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    roll_number = Column(String, unique=True, nullable=False)
    student_class = Column(String, nullable=False)
    marks = Column(Float, default=0.0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "roll_number": self.roll_number,
            "student_class": self.student_class,
            "marks": self.marks,
        }


# Ensure table exists
Base.metadata.create_all(bind=engine)

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    SessionLocal.remove()


@app.route("/")
def index():
    """Render Student Management Dashboard."""
    return render_template("index.html")


@app.route("/api/students", methods=["GET"])
def get_students():
    """Retrieve all students with optional search, filter, and summary stats."""
    db = SessionLocal()
    search = request.args.get("search", "").strip()
    student_class = request.args.get("class", "").strip()

    query = db.query(StudentDB)
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            (StudentDB.name.ilike(search_pattern))
            | (StudentDB.roll_number.ilike(search_pattern))
            | (StudentDB.student_class.ilike(search_pattern))
        )
    if student_class and student_class.lower() != "all":
        query = query.filter(StudentDB.student_class == student_class)

    students = query.order_by(StudentDB.id.asc()).all()
    student_list = [s.to_dict() for s in students]

    # Calculate statistics across all students in the database
    all_students = db.query(StudentDB).all()
    total_count = len(all_students)
    if total_count > 0:
        marks_list = [s.marks for s in all_students]
        avg_marks = round(sum(marks_list) / total_count, 1)
        max_marks = max(marks_list)
        pass_count = sum(1 for m in marks_list if m >= 40.0)
        pass_rate = round((pass_count / total_count) * 100, 1)
        classes = sorted(
            list(set(s.student_class for s in all_students if s.student_class))
        )
    else:
        avg_marks = 0.0
        max_marks = 0.0
        pass_rate = 0.0
        classes = []

    return jsonify(
        {
            "count": len(student_list),
            "data": student_list,
            "stats": {
                "total_students": total_count,
                "avg_marks": avg_marks,
                "max_marks": max_marks,
                "pass_rate": pass_rate,
                "classes": classes,
            },
        }
    )


@app.route("/api/students", methods=["POST"])
def create_student():
    """Create a new student record."""
    db = SessionLocal()
    data = request.get_json() or {}

    student_id = data.get("id")
    name = (data.get("name") or "").strip()
    roll_number = str(data.get("roll_number") or "").strip()
    student_class = (data.get("student_class") or "").strip()
    marks_raw = data.get("marks", 0.0)

    if student_id is None:
        return jsonify({"error": "Student ID is required"}), 400
    try:
        student_id = int(student_id)
    except (ValueError, TypeError):
        return jsonify({"error": "Student ID must be a valid integer"}), 400

    if not name:
        return jsonify({"error": "Student name is required"}), 400
    if not roll_number:
        return jsonify({"error": "Roll number is required"}), 400
    if not student_class:
        return jsonify({"error": "Student class is required"}), 400

    try:
        marks = float(marks_raw)
        if marks < 0 or marks > 100:
            return jsonify({"error": "Marks must be between 0 and 100"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Marks must be a valid number"}), 400

    if db.query(StudentDB).filter(StudentDB.id == student_id).first():
        return (
            jsonify({"error": f"Student with ID {student_id} already exists"}),
            400,
        )

    if db.query(StudentDB).filter(StudentDB.roll_number == roll_number).first():
        return (
            jsonify(
                {"error": f"Roll number '{roll_number}' is already registered"}
            ),
            400,
        )

    new_student = StudentDB(
        id=student_id,
        name=name,
        roll_number=roll_number,
        student_class=student_class,
        marks=marks,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return (
        jsonify(
            {
                "message": "Student created successfully",
                "data": new_student.to_dict(),
            }
        ),
        201,
    )


@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    """Retrieve a single student by ID."""
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict())


@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update an existing student record."""
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json() or {}
    name = (data.get("name") or "").strip()
    roll_number = str(data.get("roll_number") or "").strip()
    student_class = (data.get("student_class") or "").strip()
    marks_raw = data.get("marks")

    if name:
        student.name = name
    if student_class:
        student.student_class = student_class
    if roll_number:
        # Verify uniqueness
        existing = (
            db.query(StudentDB)
            .filter(
                StudentDB.roll_number == roll_number,
                StudentDB.id != student_id,
            )
            .first()
        )
        if existing:
            return (
                jsonify(
                    {
                        "error": f"Roll number '{roll_number}' is already taken by another student"
                    }
                ),
                400,
            )
        student.roll_number = roll_number
    if marks_raw is not None:
        try:
            m = float(marks_raw)
            if m < 0 or m > 100:
                return (
                    jsonify({"error": "Marks must be between 0 and 100"}),
                    400,
                )
            student.marks = m
        except (ValueError, TypeError):
            return jsonify({"error": "Marks must be a valid number"}), 400

    db.commit()
    db.refresh(student)
    return jsonify(
        {
            "message": "Student updated successfully",
            "data": student.to_dict(),
        }
    )


@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete a student record."""
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.delete(student)
    db.commit()
    return jsonify({"message": "Student deleted successfully"}), 200


if __name__ == "__main__":
    print(f"Connecting to database at: {DB_PATH}")
    print("Serving Student Management Portal on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
