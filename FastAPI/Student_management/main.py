# 🎓 FastAPI Student Management App (CRUD) - SQLite Version

# ============================================================
 
from fastapi import FastAPI, HTTPException, Depends

from pydantic import BaseModel, ConfigDict

from sqlalchemy import create_engine, Column, Integer, String, Float

from sqlalchemy.orm import declarative_base, sessionmaker, Session
 
# ------------------------------------------------------------

# 🚀 Create FastAPI App

# ------------------------------------------------------------

app = FastAPI()
 
# ------------------------------------------------------------

# 🗄️ Database Configuration

# ------------------------------------------------------------

DATABASE_URL = "sqlite:///./students.db"
 
engine = create_engine(

    DATABASE_URL, connect_args={"check_same_thread": False}

)
 
SessionLocal = sessionmaker(bind=engine)
 
Base = declarative_base()
 
# ------------------------------------------------------------

# 🧱 Database Model (Table)

# ------------------------------------------------------------

class StudentDB(Base):

    __tablename__ = "students"
 
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    roll_number = Column(String, unique=True)

    student_class = Column(String)

    marks = Column(Float, default=0.0)
 
# Create table

Base.metadata.create_all(bind=engine)
 
# ------------------------------------------------------------

# 🧾 Pydantic Schema

# ------------------------------------------------------------

class Student(BaseModel):

    model_config = ConfigDict(from_attributes=True)
 
    id: int

    name: str

    roll_number: str

    student_class: str

    marks: float = 0.0
 
# ------------------------------------------------------------

# 🔌 Dependency (DB Session)

# ------------------------------------------------------------

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
 
# ------------------------------------------------------------

# 🏠 Home Route

# ------------------------------------------------------------

@app.get("/")

def home():

    return {"message": "FastAPI Student Management with SQLite 🎓"}
 
# ------------------------------------------------------------

# ✅ 1. CREATE STUDENT

# ------------------------------------------------------------

@app.post("/students")

def create_student(student: Student, db: Session = Depends(get_db)):

    existing = db.query(StudentDB).filter(StudentDB.id == student.id).first()

    if existing:

        raise HTTPException(status_code=400, detail="ID already exists")
 
    existing_roll = db.query(StudentDB).filter(StudentDB.roll_number == student.roll_number).first()

    if existing_roll:

        raise HTTPException(status_code=400, detail="Roll number already exists")
 
    new_student = StudentDB(

        id=student.id,

        name=student.name,

        roll_number=student.roll_number,

        student_class=student.student_class,

        marks=student.marks

    )
 
    db.add(new_student)

    db.commit()

    db.refresh(new_student)
 
    return {"message": "Student created", "data": new_student}
 
# ------------------------------------------------------------

# ✅ 2. READ ALL STUDENTS

# ------------------------------------------------------------

@app.get("/students")

def get_all_students(db: Session = Depends(get_db)):

    students = db.query(StudentDB).all()

    return {"count": len(students), "data": students}
 
# ------------------------------------------------------------

# ✅ 3. READ SINGLE STUDENT

# ------------------------------------------------------------

@app.get("/students/{student_id}")

def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
 
    if not student:

        raise HTTPException(status_code=404, detail="Student not found")
 
    return student
 
# ------------------------------------------------------------

# ✅ 4. UPDATE STUDENT

# ------------------------------------------------------------

@app.put("/students/{student_id}")

def update_student(student_id: int, updated: Student, db: Session = Depends(get_db)):

    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
 
    if not student:

        raise HTTPException(status_code=404, detail="Student not found")
 
    student.name = updated.name

    student.roll_number = updated.roll_number

    student.student_class = updated.student_class

    student.marks = updated.marks
 
    db.commit()

    db.refresh(student)
 
    return {"message": "Updated successfully", "data": student}
 
# ------------------------------------------------------------

# ✅ 5. DELETE STUDENT

# ------------------------------------------------------------

@app.delete("/students/{student_id}")

def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
 
    if not student:

        raise HTTPException(status_code=404, detail="Student not found")
 
    db.delete(student)

    db.commit()
 
    return {"message": "Deleted successfully"}
 
# ------------------------------------------------------------

# ▶️ Run Server

# ------------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
 