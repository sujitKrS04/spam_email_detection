import requests

# The endpoint where your FastAPI server is listening
API_URL = "http://127.0.0.1:8000/predict"

# 1. Our base malicious email
base_email = "URGENT: Click here http://sketchy.com to claim your free prize!"

# 2. Generating counterfactuals: Systematically removing features
variations = [
    base_email,
    "Click here http://sketchy.com to claim your free prize!",  # Removed "URGENT"
    "Click here to claim your free prize!",                     # Removed the link
    "Click here to claim your prize!",                          # Removed "free"
    "Please review the attached prize document."                # Rephrased to business context
]

print("--- Automated Counterfactual Security Testing ---\n")

# 3. Fire the requests to the API and analyze the decision shifts
for text in variations:
    # Send the JSON payload to the FastAPI backend
    response = requests.post(API_URL, json={"text": text})
    
    if response.status_code == 200:
        result = response.json()
        print(f"INPUT:   '{text}'")
        print(f"VERDICT: {result['verdict']} | CONFIDENCE: {result['confidence']}")
        print("-" * 60)
    else:
        print(f"Error communicating with API: {response.status_code}")