import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError(
        "MONGO_URI is not configured. "
        "Create a .env file and add your MongoDB connection string."
    )

client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
client.admin.command("ping")

database = client["document_analyzer_db"]
analysis_collection = database["analysis"]
