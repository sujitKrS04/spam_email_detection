from fastapi import FastAPI
from pydantic import BaseModel
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast
import torch
import torch.nn.functional as F

app = FastAPI(title="SmartCastAI - BERT Engine")

# 1. Load the BERT model and tokenizer from your local folder
model_path = "./smartcast_bert_model"
tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model = DistilBertForSequenceClassification.from_pretrained(model_path)
model.eval() # Set to evaluation mode

class EmailRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict_spam(email: EmailRequest):
    # 2. Tokenize the incoming email
    inputs = tokenizer(email.text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # 3. Perform the inference
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        confidence, predicted_class = torch.max(probs, dim=1)
    
    return {
        "is_spam": bool(predicted_class.item() == 1),
        "confidence": round(confidence.item(), 4),
        "verdict": "SPAM" if predicted_class.item() == 1 else "LEGITIMATE"
    }