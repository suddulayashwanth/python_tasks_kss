# ============================================================
# Install Packages:
# pip install google-genai python-dotenv
# ============================================================

import os
from google import genai
from dotenv import load_dotenv

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Check ML Question Relevance
# ============================================================

def is_ml_related(question: str) -> bool:

    prompt = f"""
    You are a strict classifier.

    Return ONLY YES or NO.

    Return YES only if the question is related to these 5 topics:

    1. Machine Learning
    2. Deep Learning
    3. Supervised Learning
    4. Unsupervised Learning
    5. Reinforcement Learning

    Return NO for:
    - Python
    - FastAPI
    - Flask
    - Java
    - C
    - C++
    - Web Development
    - Greetings
    - Personal Questions
    - Random Text
    - Non-technical Questions

    Examples:

    Question: What is Machine Learning?
    Answer: YES

    Question: What is Deep Learning?
    Answer: YES

    Question: Explain Supervised Learning
    Answer: YES

    Question: Explain Unsupervised Learning
    Answer: YES

    Question: What is Reinforcement Learning?
    Answer: YES

    Question: What is Python?
    Answer: NO

    Question: What is FastAPI?
    Answer: NO

    Question: Hi
    Answer: NO

    Question:
    {question}

    Answer:
    """

    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config={
            "temperature": 0
        }
    )

    answer = response.text.strip().upper()

    return answer == "YES"


# ============================================================
# Generate ML Response
# ============================================================

def generate(question: str):

    # Check whether question is related to ML
    if not is_ml_related(question):

        print(
            "\n⚠️ I can answer only these 5 Machine Learning topics:\n"
            "1. Machine Learning\n"
            "2. Deep Learning\n"
            "3. Supervised Learning\n"
            "4. Unsupervised Learning\n"
            "5. Reinforcement Learning\n"
        )

        return

    # Gemini Client
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    model = "gemini-3-flash-preview"

    # ========================================================
    # System Prompt
    # ========================================================

    system_prompt = """
    You are a Machine Learning learning assistant.

    You answer questions only about these 5 topics:

    1. Machine Learning
    2. Deep Learning
    3. Supervised Learning
    4. Unsupervised Learning
    5. Reinforcement Learning

    Rules:

    - Give simple and beginner-friendly explanations.
    - Keep the answer clear and structured.
    - Give examples when useful.
    - Do not answer unrelated questions.
    - Keep answers focused on Machine Learning.
    """

    full_prompt = f"""
    {system_prompt}

    User Question:
    {question}
    """

    # ========================================================
    # Streaming Response
    # ========================================================

    print("\nAI Response:\n")

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=full_prompt
    ):
        if chunk.text:
            print(chunk.text, end="")

    print("\n")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    print("\n===== Machine Learning Assistant =====")

    print("""
You can ask questions about:

1. Machine Learning
2. Deep Learning
3. Supervised Learning
4. Unsupervised Learning
5. Reinforcement Learning
""")

    question = input("Enter your ML question: ")

    generate(question)