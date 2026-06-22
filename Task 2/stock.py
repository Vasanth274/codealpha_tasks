import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈",
    layout="centered"
)

# Custom CSS

st.markdown("""
<style>

/* Full Page Background */
.stApp {
    background: linear-gradient(
        135deg,
        #d4fc79 0%,
        #96e6a1 20%,
        #84fab0 40%,
        #8fd3f4 70%,
        #a6c1ee 100%
    );
    background-attachment: fixed;
}

.title {
    width: 100%;
    text-align: center;
    font-size: 65px;
    font-weight: 900;
    color: #0d47a1;
    letter-spacing: 2px;
    margin-top: 10px;
    margin-bottom: 5px;
    text-shadow: 2px 2px 8px rgba(255,255,255,0.7);
}
            
/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    color: #263238;
    margin-bottom: 30px;
}

/* Input Labels */
label {
    font-weight: bold !important;
    color: #1b4332 !important;
}

/* Result Box */
.result-box {
    background: linear-gradient(
        135deg,
        #43e97b,
        #38f9d7
    );
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #004d40;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}

/* Hide Streamlit Header */
header {
    visibility: hidden;
}

/* Hide Menu */
#MainMenu {
    visibility: hidden;
}

/* Hide Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    """
    <div class="title">
        📈 STOCK PORTFOLIO TRACKER
    </div>
    """,
    unsafe_allow_html=True
)

# Stock Prices Dictionary
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

# Glass Container
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.subheader("📊 Enter Stock Details")

# Input/Output
stock = st.selectbox(
    "Select Stock",
    list(stocks.keys())
)

quantity = st.number_input(
    "Enter Quantity",
    min_value=1,
    step=1
)

# Calculate Button
if st.button("🚀 Calculate Investment"):

    # Arithmetic Operation
    investment = stocks[stock] * quantity

    # Attractive Result
    st.markdown(
        f"""
        <div class="result-box">
            💰 Total Investment<br>
            ${investment}
        </div>
        """,
        unsafe_allow_html=True
    )

    # File Handling
    with open("investment.txt", "w") as file:
        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: ${investment}")

    st.success("✅ Result saved in investment.txt")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">✨ Developed using Python & Streamlit ✨</div>',
    unsafe_allow_html=True
)