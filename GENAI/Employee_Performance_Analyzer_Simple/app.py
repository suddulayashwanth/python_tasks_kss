import os
import json
import time
from pathlib import Path
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from google import genai

load_dotenv()

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./employees.db")
MONGO_URI = os.getenv("MONGO_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret_key")
ALGORITHM = "HS256"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")

if not MONGO_URI:
    raise ValueError("MONGO_URI is missing in .env")

gemini_client = genai.Client(api_key=GEMINI_API_KEY)
GEMINI_MODEL = "gemini-3.6-flash"

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["employee_performance_ai"]
analysis_collection = mongo_db["analysis"]

# ------------------------------------------------------------
# SQL Database
# ------------------------------------------------------------

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    department = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    experience = Column(Float, default=0)
    skills = Column(Text, default="")
    certifications = Column(Text, default="")
    performance_score = Column(Float, default=0)
    attendance = Column(Float, default=0)
    salary = Column(Float, default=0)
    projects_completed = Column(Integer, default=0)
    manager_feedback = Column(Text, default="")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------------------
# Schemas
# ------------------------------------------------------------

class LoginRequest(BaseModel):
    username: str
    password: str


class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str
    designation: str
    experience: float = 0
    skills: str = ""
    certifications: str = ""
    performance_score: float = 0
    attendance: float = 0
    salary: float = 0
    projects_completed: int = 0
    manager_feedback: str = ""


class EmployeeUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    department: str | None = None
    designation: str | None = None
    experience: float | None = None
    skills: str | None = None
    certifications: str | None = None
    performance_score: float | None = None
    attendance: float | None = None
    salary: float | None = None
    projects_completed: int | None = None
    manager_feedback: str | None = None


# ------------------------------------------------------------
# JWT Authentication
# ------------------------------------------------------------

security = HTTPBearer()

USERS = {
    "admin": {"password": "Admin123", "role": "Admin"},
    "hr": {"password": "HR123", "role": "HR"},
    "manager": {"password": "Manager123", "role": "Manager"},
}


def create_token(username: str, role: str):
    payload = {
        "sub": username,
        "role": role,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def employee_to_dict(emp):
    return {
        "id": emp.id,
        "employee_id": emp.employee_id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "designation": emp.designation,
        "experience": emp.experience,
        "skills": emp.skills,
        "certifications": emp.certifications,
        "performance_score": emp.performance_score,
        "attendance": emp.attendance,
        "salary": emp.salary,
        "projects_completed": emp.projects_completed,
        "manager_feedback": emp.manager_feedback,
    }


def get_employee_or_404(db: Session, employee_id: int):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


def call_gemini(prompt: str):
    last_error = None

    for attempt in range(3):
        try:
            response = gemini_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )
            if response.text:
                return response.text.strip()
        except Exception as e:
            last_error = e
            if "503" in str(e) and attempt < 2:
                time.sleep(3)
            else:
                raise

    raise Exception(last_error or "Gemini returned empty response")


# ------------------------------------------------------------
# FastAPI
# ------------------------------------------------------------

app = FastAPI(
    title="AI-Based Employee Performance Analyzer",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Employee Performance Analyzer API is running"}


@app.post("/login")
def login(data: LoginRequest):
    user = USERS.get(data.username)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_token(data.username, user["role"])

    return {
        "message": "Authentication Successful",
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }


@app.post("/employees")
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        emp = Employee(**data.model_dump())
        db.add(emp)
        db.commit()
        db.refresh(emp)

        return {
            "message": "Employee Added",
            "employee": employee_to_dict(emp)
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/employees")
def get_employees(
    department: str | None = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(Employee)

    if department:
        query = query.filter(Employee.department == department)

    return [employee_to_dict(e) for e in query.all()]


@app.get("/employees/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return employee_to_dict(get_employee_or_404(db, employee_id))


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    data: EmployeeUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    emp = get_employee_or_404(db, employee_id)

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)

    return {
        "message": "Employee Updated",
        "employee": employee_to_dict(emp)
    }


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    emp = get_employee_or_404(db, employee_id)
    db.delete(emp)
    db.commit()

    return {"message": "Employee Deleted"}


@app.post("/upload-document")
async def upload_document(
    employee_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    get_employee_or_404(db, employee_id)

    file_path = UPLOAD_DIR / file.filename
    content = await file.read()
    file_path.write_bytes(content)

    return {
        "message": "Document Uploaded",
        "employee_id": employee_id,
        "file_name": file.filename
    }


@app.post("/employee-analysis")
def employee_analysis(
    employee_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    emp = get_employee_or_404(db, employee_id)

    prompt = f"""
Analyze this employee and return ONLY valid JSON.

Employee Name: {emp.name}
Department: {emp.department}
Designation: {emp.designation}
Experience: {emp.experience}
Skills: {emp.skills}
Certifications: {emp.certifications}
Performance Score: {emp.performance_score}
Attendance: {emp.attendance}
Projects Completed: {emp.projects_completed}
Manager Feedback: {emp.manager_feedback}

Return JSON with:
summary
technical_skills
learning_path
interview_questions
career_growth_plan
training_recommendations
"""

    try:
        text = call_gemini(prompt)
        cleaned = text.replace("```json", "").replace("```", "").strip()
        analysis = json.loads(cleaned)

        analysis_collection.insert_one({
            "employee_id": employee_id,
            **analysis
        })

        return {
            "message": "Skill Analysis Completed",
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI analysis failed: {e}")


@app.post("/predict-performance")
def predict_performance(
    employee_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    emp = get_employee_or_404(db, employee_id)

    score = emp.performance_score
    attendance = emp.attendance

    if score >= 85 and attendance >= 90:
        category = "Excellent"
    elif score >= 70 and attendance >= 80:
        category = "Good"
    elif score >= 55:
        category = "Average"
    else:
        category = "Needs Improvement"

    return {
        "performance_prediction": category,
        "message": f"Performance Prediction : {category}"
    }


@app.get("/reports")
def get_reports(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    employees = db.query(Employee).all()

    return {
        "message": "Employee Report Generated Successfully",
        "total_employees": len(employees),
        "employees": [employee_to_dict(e) for e in employees]
    }
