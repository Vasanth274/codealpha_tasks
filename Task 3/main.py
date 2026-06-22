import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Smart Chatbot Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #e3f2fd,
        #bbdefb,
        #e1f5fe,
        #f3e5f5
    );
}

.title {
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#0d47a1;
}

.subtitle {
    text-align:center;
    font-size:20px;
    color:#37474f;
    margin-bottom:25px;
}

.chat-box {
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

.response {
    background:#bbdefb;
    padding:15px;
    border-radius:15px;
    color:#0d47a1;
    font-size:20px;
    font-weight:bold;
    margin-top:15px;
}

.stButton > button {
    width:100%;
    border-radius:15px;
    height:50px;
    font-size:18px;
    font-weight:bold;
    background:#42a5f5;
    color:white;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🤖 Smart Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask me simple questions!</div>',
    unsafe_allow_html=True
)

# Dictionary of Responses
responses = {
    "hello": "👋 Hello! Nice to meet you.",
    "how are you": "😊 I'm doing great!",
    "what is your name": "🤖 My name is Smart Chatbot.",
    "what is python": "🐍 Python is a popular programming language.",
    "what is html": "🌐 HTML is used to create web page structures.",
    "what is css": "🎨 CSS is used to style web pages.",
    "what is js": "⚡ JavaScript(js) makes web pages interactive.",
    "what is java": "☕ Java is a popular object-oriented programming language.",
    "what is c++": "💻 C++ is widely used for system and application development.",
    "what is ai": "🤖 AI enables machines to learn and make decisions.",
    "what is ml": "📈 Machine Learning is a branch of AI that learns from data.",
    "what is data science": "📊 Data Science involves analyzing data to gain insights.",
    "what is github": "🔗 GitHub is a platform used to store and manage code repositories.",
    "what is sql": "🗄️ SQL is used to manage and query databases.",
    "what is cloud computing": "☁️ Cloud Computing provides computing services over the internet.",
    "what is cyber security": "🔒 Cyber Security protects systems and data from cyber threats.",
    "what is an internship": "🎓 An internship provides practical work experience in a professional environment.",
    "what is a project": "💡 A project helps you apply theoretical knowledge to real-world problems.",
    "thank you": "😊 You're welcome!",
    "help": "🤝 I can answer questions about programming and technology.",
    "good morning": "🌞 Good Morning! Have a productive day.",
    "good afternoon": "☀️ Good Afternoon!",
    "good evening": "🌆 Good Evening!",
    "bye": "👋 Goodbye! Have a wonderful day."
}

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ Chat Function ------------------ #

def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "👋 Hello! Nice to meet you."

    elif "python" in user_input:
        return "🐍 Python is a beginner-friendly programming language."

    elif "ai" in user_input:
        return "🤖 AI enables machines to learn and make decisions."

    elif "name" in user_input:
        return "🤖 My name is Smart Chatbot."

    elif "streamlit" in user_input:
        return "🚀 Streamlit helps create web apps using Python."

    elif "how are you" in user_input:
        return "😊 I'm doing great! Thanks for asking."

    elif "your name" in user_input or "what is your name" in user_input:
        return "🤖 My name is Smart Chatbot."

    elif "who made you" in user_input:
        return "💻 I was created using Python and Streamlit."

    elif "python" in user_input:
        return "🐍 Python is a powerful and beginner-friendly programming language."

    elif "streamlit" in user_input:
        return "🚀 Streamlit helps create beautiful web apps using Python."

    elif "college" in user_input:
        return "🎓 College life is a great opportunity to learn and grow."

    elif "course" in user_input:
        return "📚 There are many courses available for programming and technology."

    elif "project" in user_input:
        return "💡 Projects help improve your practical coding skills."

    elif "html" in user_input:
        return "🌐 HTML is used to create web page structures."

    elif "css" in user_input:
        return "🎨 CSS is used to style web pages."

    elif "javascript" in user_input:
        return "⚡ JavaScript makes web pages interactive."

    elif "java" in user_input:
        return "☕ Java is a popular object-oriented programming language."

    elif "c++" in user_input:
        return "💻 C++ is widely used for system and application development."

    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "🤖 AI enables machines to learn and make decisions."

    elif "machine learning" in user_input:
        return "📈 Machine Learning is a branch of AI that learns from data."

    elif "data science" in user_input:
        return "📊 Data Science involves analyzing and interpreting data."

    elif "thank you" in user_input:
        return "😊 You're welcome!"

    elif "help" in user_input:
        return "🤝 I can answer questions about programming, technology, and myself."

    elif "good morning" in user_input:
        return "🌞 Good Morning! Have a wonderful day."

    elif "good afternoon" in user_input:
        return "☀️ Good Afternoon!"

    elif "good evening" in user_input:
        return "🌆 Good Evening!"

    elif "bye" in user_input:
        return "👋 Goodbye! Have a great day."

    else:
        return "❓ Sorry, I don't understand that."



# User Input
user_input = st.text_input("Type your message:")

# Buttons
col1, col2 = st.columns(2)

with col1:
    send = st.button("📩 Enter")

with col2:
    clear = st.button("🗑️ Clear Chat")

# Send Message
if send and user_input:

    reply = chatbot_response(user_input)

    st.session_state.chat_history.append(
        ("👤 You", user_input)
    )

    st.session_state.chat_history.append(
        ("🤖 Bot", reply)
    )

# Clear Chat
if clear:
    st.session_state.chat_history = []
    st.rerun()

# Chat Display
st.markdown("---")
st.subheader("💬 Chat History")

for sender, message in st.session_state.chat_history:

    if sender == "👤 You":
        st.markdown(
            f"""
            <div style="
            background:#ffca28;
            color:black;
            padding:12px;
            border-radius:15px;
            margin:8px 0;
            text-align:right;">
            <b>{sender}</b><br>{message}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div style="
            background:white;
            color:#0d47a1;
            padding:12px;
            border-radius:15px;
            margin:8px 0;
            border-left:5px solid #ffca28;">
            <b>{sender}</b><br>{message}
            </div>
            """,
            unsafe_allow_html=True
        )   