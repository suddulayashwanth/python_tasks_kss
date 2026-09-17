# ============================================================
# 🔐 FastAPI Student Management App + JWT Authentication (Array Version)
# ============================================================

# ============================================================
# 🚀 WHAT WE ARE BUILDING
# ============================================================

'''
This project includes:

✅ FastAPI
✅ JWT Authentication
✅ Student CRUD Operations (Create, Read, Update, Delete)
✅ Temporary Storage using Python List
✅ Protected APIs using Token

No Database used here.
Data will be stored temporarily in array/list.
'''

# ============================================================
# 🚀 INSTALL REQUIRED PACKAGES
# ============================================================

'''
pip install fastapi uvicorn python-jose
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List, Optional

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)

# ============================================================
# 🧾 Pydantic Models
# ============================================================

'''
Used for:
- Request validation
- Data structure
- Auto API documentation
'''

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    grade: str

# ------------------------------------------------------------

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None
    grade: Optional[str] = None

# ------------------------------------------------------------

class Login(BaseModel):
    username: str
    password: str

# ============================================================
# 🗃️ TEMPORARY DATABASE (LIST)
# ============================================================

students: List[Student] = []

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():
    return {
        "message": "FastAPI + JWT + Student Management Array CRUD 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):
    if user.username != "admin" or user.password != "admin123":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ✅ CREATE STUDENT (POST)
# ============================================================

@app.post("/students")
def create_student(
    student: Student,
    user: str = Depends(verify_token)
):
    # Check duplicate ID
    for existing in students:
        if existing.id == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    # Add student to list
    students.append(student)

    return {
        "message": "Student record created successfully",
        "data": student
    }

# ============================================================
# ✅ READ ALL STUDENTS (GET)
# ============================================================

@app.get("/students")
def get_all_students(
    user: str = Depends(verify_token)
):
    return {
        "count": len(students),
        "data": students
    }

# ============================================================
# ✅ READ SINGLE STUDENT BY ID (GET)
# ============================================================

@app.get("/students/{student_id}")
def get_student_by_id(
    student_id: int,
    user: str = Depends(verify_token)
):
    for student in students:
        if student.id == student_id:
            return {
                "data": student
            }
            
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# ✅ UPDATE STUDENT (PUT/PATCH)
# ============================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student_update: StudentUpdate,
    user: str = Depends(verify_token)
):
    for student in students:
        if student.id == student_id:
            # Only update fields that are actually passed in the request body
            if student_update.name is not None:
                student.name = student_update.name
            if student_update.age is not None:
                student.age = student_update.age
            if student_update.course is not None:
                student.course = student_update.course
            if student_update.grade is not None:
                student.grade = student_update.grade
                
            return {
                "message": f"Student with ID {student_id} updated successfully",
                "data": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# ✅ DELETE STUDENT (DELETE)
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    user: str = Depends(verify_token)
):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return {
                "message": f"Student with ID {student_id} deleted successfully",
                "data": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
