import streamlit as st
import requests

# The URL of your running FastAPI server
API_URL = "http://127.0.0.1:8000/predict"

# Page configuration with centered layout
st.set_page_config(
    page_title="SmartCastAI - Advanced Email Security",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Simple, clean CSS styling
st.markdown(
    """
<style>
    .stButton>button {
        width: 100%;
        background-color: #4A90E2;
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        border-radius: 6px;
    }
    
    .stButton>button:hover {
        background-color: #357ABD;
    }
    
    /* Simple result cards */
    .safe-card {
        background-color: #D4EDDA;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #28A745;
        color: #155724;
    }
    
    .danger-card {
        background-color: #F8D7DA;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #DC3545;
        color: #721C24;
    }
    
    .metric-card {
        background-color: #F0F0F0;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #DDD;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 0.5rem 0;
        color: #333;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #666;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Simple header
st.title("🛡️ SmartCastAI")
st.caption("Email Spam Detection using AI")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("Detect spam emails using machine learning.")

    st.divider()
    st.subheader("Sample Emails")

    sample_emails = {
        "Suspicious Email": "URGENT: Click here http://sketchy.com to claim your free prize NOW! Limited time offer!",
        "Legitimate Email": "Hi, this is a reminder about our team meeting tomorrow at 10 AM. Please review the agenda attached.",
        "Phishing Attempt": "Your account has been compromised! Verify your identity immediately at http://fake-bank.com",
    }

    selected_sample = st.selectbox(
        "Load sample:", ["None"] + list(sample_emails.keys())
    )

# Check if sample email is selected
if selected_sample != "None":
    default_text = sample_emails[selected_sample]
else:
    default_text = ""

st.divider()

# Text input box for the user
user_input = st.text_area(
    "Email Content",
    height=200,
    placeholder="Paste email text here for analysis...",
    value=default_text,
)

# Analyze button
analyze_button = st.button("Analyze Email", use_container_width=True)

# Analysis results
if analyze_button:
    if user_input.strip():
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(API_URL, json={"text": user_input})

                if response.status_code == 200:
                    result = response.json()

                    st.divider()
                    st.subheader("Results")

                    # Create two columns for results
                    col1, col2 = st.columns(2)

                    with col1:
                        # Verdict display
                        if result["verdict"] == "SPAM":
                            st.markdown(
                                """
                            <div class="danger-card">
                                <h3 style='margin:0;'>⚠️ SPAM Detected</h3>
                                <p style='margin:0.5rem 0 0 0;'>This email appears to be spam.</p>
                            </div>
                            """,
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                """
                            <div class="safe-card">
                                <h3 style='margin:0;'>✓ Legitimate Email</h3>
                                <p style='margin:0.5rem 0 0 0;'>This email appears to be safe.</p>
                            </div>
                            """,
                                unsafe_allow_html=True,
                            )

                    with col2:
                        # Confidence score
                        confidence_percentage = result["confidence"] * 100
                        st.markdown(
                            f"""
                        <div class="metric-card">
                            <div class="metric-label">Confidence Score</div>
                            <div class="metric-value">{confidence_percentage:.1f}%</div>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    # Simple stats
                    st.divider()
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric("Characters", len(user_input))
                    with col2:
                        st.metric("Words", len(user_input.split()))
                    with col3:
                        risk = "High" if result["verdict"] == "SPAM" else "Low"
                        st.metric("Risk Level", risk)

                else:
                    st.error("Error communicating with the API.")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to the API. Make sure the server is running."
                )
    else:
        st.warning("Please enter email content to analyze.")
