from config.mongo_config import analysis_collection


def save_analysis(file_name, summary, questions):
    try:
        data = {
            "file_name": file_name,
            "summary": summary,
            "interview_questions": questions
        }

        result = analysis_collection.insert_one(data)
        print("Analysis Saved to MongoDB.")

        return str(result.inserted_id)

    except Exception as e:
        raise Exception(f"MongoDB Error: {e}")
