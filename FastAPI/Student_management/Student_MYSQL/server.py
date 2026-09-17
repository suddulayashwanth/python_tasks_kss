import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)


# ==========================================
# MYSQL DATABASE CONNECTION
# ==========================================
def get_db_connection():
    password = os.getenv("MYSQL_PASSWORD", "Root")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = int(os.getenv("MYSQL_PORT", 3306))
    user = os.getenv("MYSQL_USER", "root")
    database = os.getenv("MYSQL_DATABASE", "student_db")

    try:
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error:
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password="root",
            database=database
        )


# ==========================================
# TEST SERVER
# ==========================================
@app.route("/")
def home():
    return jsonify({
        "message": "Student Management API is running"
    })


# ==========================================
# GET ALL STUDENTS
# ==========================================
@app.route("/api/students", methods=["GET"])
def get_students():

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                id,
                name,
                email,
                phone,
                course,
                department,
                year
            FROM students
            ORDER BY id
        """)

        students = cursor.fetchall()

        return jsonify(students), 200

    except Exception as e:

        print("GET ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# ==========================================
# ADD STUDENT
# ==========================================
@app.route("/api/students", methods=["POST"])
def add_student():

    data = request.get_json()

    print("DATA RECEIVED:", data)

    if not data:
        return jsonify({
            "error": "Student data is required"
        }), 400

    conn = None
    cursor = None

    try:

        conn = get_db_connection()

        print("MYSQL CONNECTED")

        cursor = conn.cursor()

        sql = """
            INSERT INTO students
            (
                name,
                email,
                phone,
                course,
                department,
                year
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("course"),
            data.get("department"),
            data.get("year")
        )

        cursor.execute(sql, values)

        conn.commit()

        student_id = cursor.lastrowid

        print("STUDENT INSERTED:", student_id)

        return jsonify({
            "id": student_id,
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "course": data.get("course"),
            "department": data.get("department"),
            "year": data.get("year")
        }), 201

    except Exception as e:

        if conn:
            conn.rollback()

        print("POST ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# ==========================================
# UPDATE STUDENT
# ==========================================
@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Student data is required"
        }), 400

    conn = None
    cursor = None

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE students
            SET
                name = %s,
                email = %s,
                phone = %s,
                course = %s,
                department = %s,
                year = %s
            WHERE id = %s
        """

        values = (
            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("course"),
            data.get("department"),
            data.get("year"),
            student_id
        )

        cursor.execute(sql, values)

        conn.commit()

        if cursor.rowcount == 0:

            return jsonify({
                "error": "Student not found"
            }), 404

        return jsonify({
            "message": "Student updated successfully"
        }), 200

    except Exception as e:

        if conn:
            conn.rollback()

        print("UPDATE ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# ==========================================
# DELETE STUDENT
# ==========================================
@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    conn = None
    cursor = None

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = %s",
            (student_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:

            return jsonify({
                "error": "Student not found"
            }), 404

        return jsonify({
            "message": "Student deleted successfully"
        }), 200

    except Exception as e:

        if conn:
            conn.rollback()

        print("DELETE ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# ==========================================
# RUN SERVER
# ==========================================
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )