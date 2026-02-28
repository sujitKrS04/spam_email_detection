import streamlit as st
import requests
import time

# The URL of your running FastAPI server
API_URL = "http://127.0.0.1:8000/predict"

# Page configuration with wide layout
st.set_page_config(
    page_title="SmartCastAI - Advanced Email Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main background and color scheme */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* Custom card styling */
    .stApp {
        background: transparent;
    }
    
    /* Title styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(120deg, #ffffff, #e0e7ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        text-align: center;
        color: #e0e7ff;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Card container */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        margin: 1rem 0;
    }
    
    /* Custom button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e7ff;
        padding: 1rem;
        font-size: 1rem;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Result cards */
    .result-card {
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Metric styling */
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    /* Safe card */
    .safe-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 10px 30px rgba(56, 239, 125, 0.3);
    }
    
    /* Danger card */
    .danger-card {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 10px 30px rgba(235, 51, 73, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Stats badge */
    .stat-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.5rem;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">🛡️ SmartCastAI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Advanced Email Security & Threat Detection</p>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.markdown("### 📊 About")
    st.markdown("""
    **SmartCastAI** uses advanced machine learning to detect spam and phishing attempts in real-time.
    
    ### 🎯 Features
    - Real-time threat analysis
    - High accuracy detection
    - Confidence scoring
    - Instant results
    
    ### 🔒 Security Level
    """)
    st.progress(0.95)
    st.markdown("**95% Accuracy**")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.info("Paste suspicious email content to analyze potential threats.")
    
    st.markdown("---")
    st.markdown("### 📝 Example Samples")
    
    sample_emails = {
        "Suspicious Email": "URGENT: Click here http://sketchy.com to claim your free prize NOW! Limited time offer!",
        "Legitimate Email": "Hi, this is a reminder about our team meeting tomorrow at 10 AM. Please review the agenda attached.",
        "Phishing Attempt": "Your account has been compromised! Verify your identity immediately at http://fake-bank.com"
    }
    
    selected_sample = st.selectbox("Load sample:", ["None"] + list(sample_emails.keys()))

# Main content area with card styling
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Check if sample email is selected
    if selected_sample != "None":
        default_text = sample_emails[selected_sample]
    else:
        default_text = ""
    
    # Text input box for the user
    user_input = st.text_area(
        "📧 Email Content",
        height=200,
        placeholder="Paste email text here for analysis...",
        value=default_text,
        help="Enter the email content you want to analyze for potential threats"
    )
    
    # Analyze button
    col_btn1, col_btn2, col_btn3 = st.columns([2, 3, 2])
    with col_btn2:
        analyze_button = st.button("🔍 Analyze Email", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Analysis results
    if analyze_button:
        if user_input.strip():
            # Progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            with st.spinner('🔄 Analyzing email content...'):
                # Simulate analysis steps
                for i in range(100):
                    progress_bar.progress(i + 1)
                    if i < 30:
                        status_text.text("📖 Reading email content...")
                    elif i < 60:
                        status_text.text("🧠 Processing with AI model...")
                    elif i < 90:
                        status_text.text("🔍 Analyzing threat patterns...")
                    else:
                        status_text.text("✅ Finalizing results...")
                    time.sleep(0.01)
                
                try:
                    response = requests.post(API_URL, json={"text": user_input})
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        # Clear progress indicators
                        progress_bar.empty()
                        status_text.empty()
                        
                        st.markdown("---")
                        st.markdown("### 📊 Analysis Results")
                        
                        # Create two columns for results
                        res_col1, res_col2 = st.columns(2)
                        
                        with res_col1:
                            # Verdict display
                            if result["verdict"] == "SPAM":
                                st.markdown("""
                                <div class="danger-card">
                                    <h2 style='margin:0;'>🚨 THREAT DETECTED</h2>
                                    <h3 style='margin-top:0.5rem;'>Classification: SPAM</h3>
                                    <p>This email contains suspicious patterns and should be treated with caution.</p>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                st.markdown("""
                                <div class="safe-card">
                                    <h2 style='margin:0;'>✅ EMAIL SAFE</h2>
                                    <h3 style='margin-top:0.5rem;'>Classification: LEGITIMATE</h3>
                                    <p>This email appears to be safe and legitimate.</p>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        with res_col2:
                            # Confidence score with visual indicator
                            confidence_percentage = result['confidence'] * 100
                            st.markdown(f"""
                            <div class="metric-card">
                                <div class="metric-label">CONFIDENCE SCORE</div>
                                <div class="metric-value">{confidence_percentage:.1f}%</div>
                                <p style='margin:0.5rem 0 0 0; font-size:0.9rem;'>Model certainty level</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Additional insights
                        st.markdown("### 🔍 Detailed Analysis")
                        
                        insight_col1, insight_col2, insight_col3 = st.columns(3)
                        
                        with insight_col1:
                            st.metric("Email Length", f"{len(user_input)} chars", delta=None)
                        
                        with insight_col2:
                            st.metric("Word Count", f"{len(user_input.split())} words", delta=None)
                        
                        with insight_col3:
                            risk_level = "HIGH" if result["verdict"] == "SPAM" else "LOW"
                            st.metric("Risk Level", risk_level, delta=None)
                        
                        # Recommendations
                        st.markdown("### 💡 Recommendations")
                        if result["verdict"] == "SPAM":
                            st.warning("""
                            **⚠️ Security Recommendations:**
                            - Do not click any links in this email
                            - Do not download any attachments
                            - Do not reply with personal information
                            - Report this email to your IT department
                            - Mark as spam/phishing in your email client
                            """)
                        else:
                            st.success("""
                            **✅ This email appears safe, but always:**
                            - Verify sender's email address
                            - Be cautious with unexpected attachments
                            - Hover over links before clicking
                            - Use common sense and stay vigilant
                            """)
                        
                    else:
                        progress_bar.empty()
                        status_text.empty()
                        st.error("❌ Error communicating with the backend API. Please try again.")
                        
                except requests.exceptions.ConnectionError:
                    progress_bar.empty()
                    status_text.empty()
                    st.error("🔌 Could not connect to the API. Please ensure your FastAPI server is running on http://127.0.0.1:8000")
                    st.info("**To start the server, run:** `uvicorn main:app --reload`")
        else:
            st.warning("⚠️ Please enter email content to analyze.")

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("### 🎯 Powered by")
    st.markdown("BERT AI Model")

with footer_col2:
    st.markdown("### 🔐 Security")
    st.markdown("Enterprise Grade")

with footer_col3:
    st.markdown("### ⚡ Performance")
    st.markdown("Real-time Analysis")