# ============================================================
# 🎓 FastAPI Student Management - MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo certifi
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField
import certifi

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
import os
import certifi

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise RuntimeError("MONGO_URL environment variable is not set")

connect(
    host=MONGO_URL,
    tlsCAFile=certifi.where()
)
# ------------------------------------------------------------
# 🧱 MongoDB Student Model
# ------------------------------------------------------------
class StudentDB(Document):
    id = IntField(primary_key=True)
    name = StringField(required=True)
    age = IntField(required=True)
    course = StringField(required=True)

    meta = {
        "collection": "students"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# ------------------------------------------------------------
# 🏠 HOME
# ------------------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "FastAPI + MongoDB Student Management 🚀"
    }

# ------------------------------------------------------------
# ✅ 1. CREATE STUDENT
# ------------------------------------------------------------
@app.post("/students")
def create_student(student: Student):

    existing = StudentDB.objects(id=student.id).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        id=student.id,
        name=student.name,
        age=student.age,
        course=student.course
    )

    new_student.save()

    return {
        "message": "Student created successfully",
        "data": student
    }

# ------------------------------------------------------------
# ✅ 2. READ ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_all_students():

    students = StudentDB.objects()

    data = []

    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ 3. READ SINGLE STUDENT
# ------------------------------------------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = StudentDB.objects(id=student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

# ------------------------------------------------------------
# ✅ 4. UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):

    student = StudentDB.objects(id=student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated.name
    student.age = updated.age
    student.course = updated.course

    student.save()

    return {
        "message": "Student updated successfully"
    }

# ------------------------------------------------------------
# ✅ 5. DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    student = StudentDB.objects(id=student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }