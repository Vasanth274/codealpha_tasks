import streamlit as st
import random

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Hangman GAME",
    page_icon="🎮",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #f8fafc,
        #e0f2fe,
        #dbeafe
    );
}

/* Title */
.title{
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:#2563eb;
    margin-bottom:10px;
}

/* Main Card */
.card{
    background:white;
    padding:30px;
    border-radius:25px;
    text-align:center;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.1);

    border:1px solid #e5e7eb;
}

/* Word */
.word{
    font-size:50px;
    font-weight:bold;
    letter-spacing:14px;
    color:#16a34a;
}

/* Stats */
.stats{
    text-align:center;
    font-size:22px;
    color:#334155;
    margin-top:20px;
    font-weight:600;
}

/* Buttons */
.stButton > button{

    background:linear-gradient(
        45deg,
        #3b82f6,
        #2563eb
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:12px !important;

    font-weight:bold !important;

    transition:0.3s !important;
}

.stButton > button:hover{
    transform:scale(1.05);
}

/* Footer */
.footer{
    text-align:center;
    color:#64748b;
    margin-top:20px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- WORDS ----------------
WORDS = [
    "table",
    "chair",
    "mango",
    "water",
    "watch",
    "smile",
    "river",
    "plant",
    "tiger",
    "apple"
]

# ---------------- SESSION STATE ----------------
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)

if "guessed" not in st.session_state:
    st.session_state.guessed = []

if "wrong" not in st.session_state:
    st.session_state.wrong = 0

# ---------------- TITLE ----------------
st.markdown(
    "<div class='title'>🎮 HANGMAN GAME</div>",
    unsafe_allow_html=True
)

# ---------------- WORD DISPLAY ----------------
display_word = ""

for letter in st.session_state.word:
    if letter in st.session_state.guessed:
        display_word += letter.upper() + " "
    else:
        display_word += "_ "

st.markdown(
    f"""
    <div class="card">
        <div class="word">{display_word}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- STATS ----------------
lives = 6 - st.session_state.wrong

st.markdown(
    f"""
    <div class='stats'>
        ❤️ Lives Left: {lives}
        <br>
        🔤 Used Letters:
        {' '.join(st.session_state.guessed)}
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CHECK WIN ----------------
won = all(
    letter in st.session_state.guessed
    for letter in st.session_state.word
)

lost = st.session_state.wrong >= 6

if won:
    st.success("🏆 CONGRATULATIONS! YOU WON!")
    st.balloons()

if lost:
    st.error(
        f"💀 GAME OVER! The word was: {st.session_state.word.upper()}"
    )

# ---------------- LETTER BUTTONS ----------------
if not won and not lost:

    st.write("### 🎯 Choose a Letter")

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cols = st.columns(13)

    for i, letter in enumerate(letters):

        lower = letter.lower()

        disabled = lower in st.session_state.guessed

        if cols[i % 13].button(
            letter,
            key=letter,
            disabled=disabled,
            use_container_width=True
        ):

            st.session_state.guessed.append(lower)

            if lower not in st.session_state.word:
                st.session_state.wrong += 1

            st.rerun()

# ---------------- RESTART ----------------
st.markdown("---")

if st.button(
    "🔄 Play Again",
    use_container_width=True
):
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.rerun()

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class='footer'>
    ✨ CodeAlpha Python Internship Project ✨
    </div>
    """,
    unsafe_allow_html=True
)