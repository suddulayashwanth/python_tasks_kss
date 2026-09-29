import os

from utils.file_reader import read_document
from service.document_service import analyze_document


def main():
    file_path = "documents/sample.txt"

    try:
        document = read_document(file_path)
        file_name = os.path.basename(file_path)

        result = analyze_document(
            file_name=file_name,
            document=document
        )

        print("\n" + "=" * 60)
        print("DOCUMENT SUMMARY")
        print("=" * 60)
        print(result["summary"])

        print("\n" + "=" * 60)
        print("INTERVIEW QUESTIONS")
        print("=" * 60)
        print(result["questions"])

        print("\nOperation Completed Successfully.")

    except Exception as e:
        print(f"\nOperation Failed: {e}")


if __name__ == "__main__":
    main()
