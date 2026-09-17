from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from urllib.parse import quote_plus
import certifi


# ==================================================
# FLASK APP
# ==================================================

app = Flask(__name__)

CORS(app)


# ==================================================
# MONGODB ATLAS CONNECTION
# ==================================================

USERNAME = "YASWANTH"

# Put your NEW MongoDB Atlas password here
PASSWORD = "Yash9502M"

CLUSTER = "cluster0.qk1xln0.mongodb.net"


# Encode username and password
USERNAME = quote_plus(USERNAME)
PASSWORD = quote_plus(PASSWORD)

# ==================================================
# MONGODB CONNECTION STRING
# ==================================================

MONGO_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER}/?retryWrites=true&w=majority&appName=Cluster0"

# ==================================================
# CREATE MONGODB CLIENT
# ==================================================

client = MongoClient(
    MONGO_URI,

    # Enable TLS/SSL
    tls=True,

    # Use trusted CA certificates
    tlsCAFile=certifi.where(),

    # Connection timeout
    connectTimeoutMS=10000,

    # Server selection timeout
    serverSelectionTimeoutMS=10000
)


# ==================================================
# DATABASE
# ==================================================

db = client["student_db"]


# ==================================================
# COLLECTION
# ==================================================

students_collection = db["students"]


# ==================================================
# TEST MONGODB CONNECTION
# ==================================================

try:

    client.admin.command("ping")

    print("--------------------------------------")
    print("MongoDB Atlas connected successfully!")
    print("Database   : student_db")
    print("Collection : students")
    print("--------------------------------------")

except Exception as e:

    print("--------------------------------------")
    print("MongoDB connection failed!")
    print("Error:", e)
    print("--------------------------------------")


# ==================================================
# HOME / TEST API
# ==================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Student Management API is running",
        "database": "MongoDB Atlas"
    })


# ==================================================
# CONVERT MONGODB DOCUMENT TO JSON
# ==================================================

def student_response(student):

    return {
        "id": str(student["_id"]),
        "name": student.get("name", ""),
        "email": student.get("email", ""),
        "phone": student.get("phone", ""),
        "course": student.get("course", ""),
        "department": student.get("department", ""),
        "year": student.get("year", "")
    }


# ==================================================
# GET ALL STUDENTS
# ==================================================

@app.route("/api/students", methods=["GET"])
def get_students():

    try:

        students = students_collection.find().sort("_id", 1)

        result = []

        for student in students:

            result.append(
                student_response(student)
            )

        return jsonify(result), 200

    except Exception as e:

        print("GET ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


# ==================================================
# ADD STUDENT
# ==================================================

@app.route("/api/students", methods=["POST"])
def add_student():

    try:

        data = request.get_json()

        print("--------------------------------------")
        print("DATA RECEIVED:", data)
        print("--------------------------------------")

        if not data:

            return jsonify({
                "error": "Student data is required"
            }), 400


        # Create student document
        student = {

            "name": data.get("name", ""),

            "email": data.get("email", ""),

            "phone": data.get("phone", ""),

            "course": data.get("course", ""),

            "department": data.get("department", ""),

            "year": data.get("year", "")
        }


        # Insert into MongoDB
        result = students_collection.insert_one(student)


        # Add MongoDB ID
        student["_id"] = result.inserted_id


        print("--------------------------------------")
        print("STUDENT INSERTED")
        print("ID:", result.inserted_id)
        print("--------------------------------------")


        return jsonify(
            student_response(student)
        ), 201


    except Exception as e:

        print("POST ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


# ==================================================
# UPDATE STUDENT
# ==================================================


def get_student_query(student_id):
    query_ids = []
    if ObjectId.is_valid(student_id):
        query_ids.append(ObjectId(student_id))
    if str(student_id).isdigit():
        query_ids.append(int(student_id))
    query_ids.append(str(student_id))
    return {"_id": {"$in": query_ids}}


# ==================================================
# UPDATE STUDENT
# ==================================================

@app.route("/api/students/<student_id>", methods=["PUT"])
def update_student(student_id):

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error": "Student data is required"
            }), 400


        # Update student
        result = students_collection.update_one(

            get_student_query(student_id),

            {
                "$set": {

                    "name": data.get("name", ""),

                    "email": data.get("email", ""),

                    "phone": data.get("phone", ""),

                    "course": data.get("course", ""),

                    "department": data.get("department", ""),

                    "year": data.get("year", "")
                }
            }
        )


        if result.matched_count == 0:

            return jsonify({
                "error": "Student not found"
            }), 404


        print("--------------------------------------")
        print("STUDENT UPDATED")
        print("ID:", student_id)
        print("--------------------------------------")


        return jsonify({
            "message": "Student updated successfully"
        }), 200


    except Exception as e:

        print("UPDATE ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


# ==================================================
# DELETE STUDENT
# ==================================================

@app.route("/api/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):

    try:

        # Delete student
        result = students_collection.delete_one(
            get_student_query(student_id)
        )


        if result.deleted_count == 0:

            return jsonify({
                "error": "Student not found"
            }), 404


        print("--------------------------------------")
        print("STUDENT DELETED")
        print("ID:", student_id)
        print("--------------------------------------")


        return jsonify({
            "message": "Student deleted successfully"
        }), 200


    except Exception as e:

        print("DELETE ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


# ==================================================
# RUN SERVER
# ==================================================

if __name__ == "__main__":

    print("--------------------------------------")
    print("Starting Student Management API...")
    print("API URL: http://127.0.0.1:5000")
    print("--------------------------------------")


    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )