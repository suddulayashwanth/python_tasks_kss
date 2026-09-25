def read_document(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            document = file.read()

        if not document.strip():
            raise ValueError("Document is empty.")

        print("Document Read Successfully.")
        return document

    except FileNotFoundError:
        raise Exception(f"Document file not found: {file_path}")

    except Exception as e:
        raise Exception(f"Error reading document: {e}")
