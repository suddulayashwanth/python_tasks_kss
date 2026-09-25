
# ============================================================
# 🚀 Advanced GPT Style Flask Chat UI
# ============================================================

# Install Packages:
# pip install flask requests

from flask import Flask, render_template_string, request, jsonify
import requests

# ============================================================
# Flask App
# ============================================================

app = Flask(__name__)

# ============================================================
# FastAPI Backend URL
# ============================================================

FASTAPI_URL = "http://127.0.0.1:8000/ask"

# ============================================================
# HTML PAGE
# ============================================================

HTML_PAGE = """

<html>

<head>

    <title>GPT Chat UI</title>

    <style>

        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body{
            background-color: #0f172a;
            font-family: Arial, sans-serif;
            color: white;
        }

        .chat-container{
            width: 100%;
            max-width: 1000px;
            margin: auto;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .header{
            padding: 20px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            border-bottom: 1px solid #1e293b;
            background-color: #111827;
        }

        .messages{
            flex: 1;
            overflow-y: auto;
            padding: 25px;
        }

        .message{
            display: flex;
            margin-bottom: 25px;
            align-items: flex-start;
        }

        .user{
            justify-content: flex-end;
        }

        .bot{
            justify-content: flex-start;
        }

        .bubble{
            max-width: 70%;
            padding: 15px 20px;
            border-radius: 15px;
            line-height: 1.6;
            font-size: 16px;
            word-wrap: break-word;
        }

        .user .bubble{
            background-color: #2563eb;
            color: white;
            border-bottom-right-radius: 5px;
        }

        .bot .bubble{
            background-color: #1e293b;
            color: white;
            border-bottom-left-radius: 5px;
        }

        .icon{
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 22px;
            margin: 0 12px;
        }

        .user .icon{
            background-color: #2563eb;
        }

        .bot .icon{
            background-color: #10b981;
        }

        .input-box{
            padding: 20px;
            border-top: 1px solid #1e293b;
            background-color: #111827;
        }

        form{
            display: flex;
            gap: 10px;
        }

        input{
            flex: 1;
            padding: 15px;
            border-radius: 12px;
            border: none;
            outline: none;
            font-size: 16px;
            background-color: #1e293b;
            color: white;
        }

        button{
            padding: 15px 25px;
            border: none;
            border-radius: 12px;
            background-color: #2563eb;
            color: white;
            cursor: pointer;
            font-size: 16px;
        }

        button:disabled{
            opacity: 0.6;
            cursor: not-allowed;
        }

        .typing{
            display: flex;
            gap: 5px;
            align-items: center;
        }

        .dot{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: white;
            animation: bounce 1.3s infinite;
        }

        .dot:nth-child(2){
            animation-delay: 0.2s;
        }

        .dot:nth-child(3){
            animation-delay: 0.4s;
        }

        @keyframes bounce{
            0%, 80%, 100%{
                transform: scale(0.7);
                opacity: 0.5;
            }

            40%{
                transform: scale(1);
                opacity: 1;
            }
        }

    </style>

</head>

<body>

    <div class="chat-container">

        <div class="header">
            🤖 Gemini GPT Chat
        </div>

        <div class="messages" id="messages">

        </div>

        <div class="input-box">

            <form id="chat-form">

                <input
                    type="text"
                    id="question"
                    placeholder="Ask something..."
                    autocomplete="off"
                    required
                >

                <button type="submit" id="send-btn">
                    Send
                </button>

            </form>

        </div>

    </div>

<script>


// DOM Elements - Document Obj Model

const form = document.getElementById("chat-form");
const input = document.getElementById("question");
const messages = document.getElementById("messages");
const sendBtn = document.getElementById("send-btn");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const question = input.value.trim();

    if(question === ""){
        return;
    }

    // =====================================================
    // Disable Button
    // =====================================================

    sendBtn.disabled = true;

    // =====================================================
    // Add User Message
    // =====================================================

    messages.innerHTML += `
        <div class="message user">
            <div class="bubble">${question}</div>
            <div class="icon">👤</div>
        </div>
    `;

    // =====================================================
    // Add Loading Message
    // =====================================================

    const loadingId = "loading-" + Date.now();

    messages.innerHTML += `
        <div class="message bot" id="${loadingId}">
            <div class="icon">🤖</div>

            <div class="bubble">
                <div class="typing">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            </div>
        </div>
    `;

    // =====================================================
    // Auto Scroll
    // =====================================================

    messages.scrollTop = messages.scrollHeight;

    // =====================================================
    // Clear Input
    // =====================================================

    input.value = "";

    try{

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        // =================================================
        // Replace Loading with Response
        // =================================================

        document.getElementById(loadingId).innerHTML = `
            <div class="icon">🤖</div>

            <div class="bubble">
                ${data.response}
            </div>
        `;

    }
    catch(error){

        document.getElementById(loadingId).innerHTML = `
            <div class="icon">🤖</div>

            <div class="bubble">
                Error: ${error}
            </div>
        `;
    }

    // =====================================================
    // Enable Button Again
    // =====================================================

    sendBtn.disabled = false;

    messages.scrollTop = messages.scrollHeight;

});

</script>

</body>
</html>

"""

# ============================================================
# Home Route
# ============================================================

@app.route("/")
def home():

    return render_template_string(HTML_PAGE)

# ============================================================
# API Route
# ============================================================

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question")

    try:

        response = requests.post(
            FASTAPI_URL,
            json={
                "question": question
            }
        )

        result = response.json()

        return jsonify({
            "response": result.get("response")
        })

    except Exception as e:

        return jsonify({
            "response": str(e)
        })

# ============================================================
# Run Flask App
# ============================================================

if __name__ == "__main__":

    app.run(debug=True, port=5000)
