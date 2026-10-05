import streamlit as st
import requests

st.set_page_config(
    page_title="GEN AI Assistant",
    page_icon="🤖",
    layout="centered"
)

FASTAPI_URL = "http://127.0.0.1:8000/ask"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processing" not in st.session_state:
    st.session_state.processing = False


st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f8fa;
    }

    .main-title {
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        color: #222222;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 15px;
        color: #666666;
        margin-bottom: 30px;
    }

    .user-box {
        background-color: #e8f0fe;
        border: 1px solid #c5d7f2;
        border-radius: 12px;
        padding: 14px 18px;
        margin: 10px 0;
        color: #1f2937;
        font-size: 16px;
    }

    .ai-box {
        background-color: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 12px;
        padding: 14px 18px;
        margin: 10px 0 20px 0;
        color: #222222;
        font-size: 16px;
        line-height: 1.6;
    }

    .section-title {
        font-size: 18px;
        font-weight: 600;
        color: #333333;
        margin-top: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title">🤖 GEN AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask questions and get answers from Gemini AI</div>',
    unsafe_allow_html=True
)


with st.sidebar:

    st.header("GEN AI")

    st.write("Your AI Assistant")

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.session_state.processing = False
        st.rerun()

    st.divider()

    st.subheader("About")

    st.write(
        "This application uses a "
        "FastAPI backend and Gemini AI "
        "to answer your questions."
    )

    st.divider()

    st.write("**Backend:** FastAPI")
    st.write("**AI:** Gemini")
    st.write("**Frontend:** Streamlit")


if len(st.session_state.messages) == 0:

    st.markdown(
        '<div class="section-title">Try asking:</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="ai-box">
        💡 What is Artificial Intelligence?
        </div>

        <div class="ai-box">
        🐍 Explain Python programming
        </div>

        <div class="ai-box">
        🧠 What is Machine Learning?
        </div>

        <div class="ai-box">
        🚀 Give me an AI project idea
        </div>
        """,
        unsafe_allow_html=True
    )


for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-box">
            <strong>👤 You</strong><br><br>
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="ai-box">
            <strong>🤖 Gemini AI</strong><br><br>
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


question = st.chat_input(
    "Type your question here..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.session_state.processing = True

    st.rerun()


if st.session_state.processing:

    last_message = st.session_state.messages[-1]

    if last_message["role"] == "user":

        with st.spinner("Gemini is thinking..."):

            try:

                response = requests.post(
                    FASTAPI_URL,
                    json={
                        "question": last_message["content"]
                    },
                    timeout=120
                )

                if response.status_code == 200:

                    data = response.json()

                    answer = data.get(
                        "response",
                        "No response received."
                    )

                else:

                    answer = (
                        "Backend returned error "
                        f"{response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                answer = (
                    "❌ Cannot connect to the FastAPI server.\n\n"
                    "Please start your FastAPI backend first."
                )

            except requests.exceptions.Timeout:

                answer = (
                    "⏳ The request took too long. "
                    "Please try again."
                )

            except Exception as e:

                answer = f"❌ Error: {str(e)}"

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.session_state.processing = False

        st.rerun()