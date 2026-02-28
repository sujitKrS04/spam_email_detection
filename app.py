import streamlit as st
import requests

# The URL of your running FastAPI server
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="SmartCastAI Spam Filter", page_icon="🛡️")

st.title("🛡️ SmartCastAI Threat Detection")
st.markdown("Enter an email below to analyze its threat level and test counterfactual variations.")

# Text input box for the user
user_input = st.text_area("Email Content:", height=150, placeholder="Paste email text here...")

if st.button("Analyze Threat Level"):
    if user_input.strip():
        # Send the text to your FastAPI backend
        with st.spinner('Analyzing...'):
            try:
                response = requests.post(API_URL, json={"text": user_input})
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.divider()
                    # Display results with dynamic colors
                    if result["verdict"] == "SPAM":
                        st.error(f"🚨 **VERDICT: {result['verdict']}**")
                    else:
                        st.success(f"✅ **VERDICT: {result['verdict']}**")
                        
                    st.info(f"**Confidence Score:** {result['confidence'] * 100:.2f}%")
                    
                else:
                    st.error("Error communicating with the backend API.")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the API. Is your FastAPI server running?")
    else:
        st.warning("Please enter some text to analyze.")