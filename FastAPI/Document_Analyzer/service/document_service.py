import time

from config.gemini_config import client
from repository.analysis_repository import save_analysis

MODEL_NAME = "gemini-3.6-flash"


def generate_analysis(document):
    try:
        prompt = f"""
Analyze the following document.

Do these two tasks:

1. Generate a clear and concise summary of the document.
2. Generate exactly 5 interview questions based on the document.

Return the response exactly in this format:

SUMMARY:
<summary here>

INTERVIEW QUESTIONS:
1. <question>
2. <question>
3. <question>
4. <question>
5. <question>

Document:
{document}
"""

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                if response.text:
                    return response.text.strip()

            except Exception as e:
                if "503" in str(e) and attempt < 2:
                    print("Gemini is busy. Retrying...")
                    time.sleep(3)
                else:
                    raise e

        raise Exception("Gemini did not return a response.")

    except Exception as e:
        raise Exception(f"Gemini Analysis Error: {e}")


def split_analysis(response_text):
    try:
        if "INTERVIEW QUESTIONS:" not in response_text:
            raise ValueError("Unexpected Gemini response format.")

        parts = response_text.split("INTERVIEW QUESTIONS:", 1)

        summary = parts[0].replace("SUMMARY:", "").strip()

        questions = parts[1].strip()

        return summary, questions

    except Exception as e:
        raise Exception(f"Response Processing Error: {e}")


def analyze_document(file_name, document):
    try:
        response = generate_analysis(document)

        summary, questions = split_analysis(response)

        print("Document Summary Generated Successfully.")
        print("Interview Questions Generated Successfully.")

        document_id = save_analysis(
            file_name=file_name,
            summary=summary,
            questions=questions
        )

        return {
            "id": document_id,
            "summary": summary,
            "questions": questions
        }

    except Exception as e:
        raise Exception(f"Document Analysis Error: {e}")