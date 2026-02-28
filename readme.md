# 🛡️ SmartCastAI - Advanced Email Security & Threat Detection

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**SmartCastAI** is an end-to-end machine learning pipeline and web application designed to identify malicious email content with high precision. Originally developed as a Random Forest baseline, the system was upgraded to a fine-tuned **DistilBERT Transformer model** to achieve industry-grade recall and semantic understanding.

</div>

---

## ✨ Features

- 🎯 **High Accuracy Detection** - 95%+ accuracy using fine-tuned BERT model
- ⚡ **Real-time Analysis** - Instant threat detection and classification
- 🎨 **Beautiful UI** - Modern, professional interface with smooth animations
- 📊 **Confidence Scoring** - Detailed probability metrics for each prediction
- 🔍 **Detailed Analysis** - Comprehensive email statistics and insights
- 💡 **Smart Recommendations** - Context-aware security suggestions
- 🧪 **Sample Testing** - Pre-loaded examples for quick testing
- 🔒 **Enterprise-Grade** - Production-ready API with FastAPI backend

---

## 🖼️ Interface Preview

The application features a stunning, modern interface with:
- **Gradient backgrounds** with purple/blue theme
- **Animated result cards** with smooth transitions
- **Color-coded threat levels** (red for spam, green for safe)
- **Interactive metrics** and confidence scores
- **Sidebar navigation** with helpful tips and samples
- **Responsive design** that works on all screen sizes

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sujitKrS04/spam_email_detection.git
   cd spam_email_detection
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit fastapi uvicorn transformers torch requests
   ```

3. **Download the model** (if not included)
   > Note: The `model.safetensors` file is too large for GitHub. Download it separately from the provided link or train your own model.

### Running the Application

You need to run **two servers** simultaneously:

#### Terminal 1: Start the FastAPI Backend
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

This will start the API server at `http://127.0.0.1:8000`

#### Terminal 2: Start the Streamlit Frontend
```bash
streamlit run app.py
```

This will open the web interface at `http://localhost:8501`

---

## 📖 Usage Guide

### Using the Web Interface

1. **Open the application** in your browser (usually `http://localhost:8501`)
2. **Enter email content** in the text area, or select a sample from the sidebar
3. **Click "Analyze Email"** to start the analysis
4. **View the results** including:
   - Threat classification (SPAM or LEGITIMATE)
   - Confidence score percentage
   - Email statistics
   - Security recommendations

### Using the API Directly

You can also use the FastAPI backend directly:

```python
import requests

API_URL = "http://127.0.0.1:8000/predict"

response = requests.post(API_URL, json={
    "text": "Your email content here"
})

result = response.json()
print(f"Verdict: {result['verdict']}")
print(f"Confidence: {result['confidence']}")
```

### Testing with Client Script

Run the automated counterfactual testing:

```bash
python client.py
```

This will test various email variations and show how the model responds to different patterns.

---

## 🏗️ Project Structure

```
spam_email_detection/
├── app.py                          # Streamlit frontend (beautiful UI)
├── main.py                         # FastAPI backend server
├── client.py                       # Automated testing script
├── smartcast_bert_model/           # Fine-tuned BERT model
│   ├── config.json
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   └── model.safetensors          # (Not in repo - too large)
├── README.md                       # This file
└── LICENSE                         # License information
```

---

## 🧠 Model Architecture

### Technology Stack
- **Base Model**: DistilBERT (distilbert-base-uncased)
- **Framework**: Hugging Face Transformers
- **Backend**: FastAPI for high-performance API
- **Frontend**: Streamlit with custom CSS
- **Inference**: PyTorch

### Training Details
- Fine-tuned on spam/ham email dataset
- Binary classification (SPAM vs LEGITIMATE)
- Optimized for both precision and recall
- Model size: ~250MB

---

## 🎨 UI Customization

The interface uses custom CSS with:
- Gradient backgrounds
- Card-based layouts
- Smooth animations
- Responsive design
- Color-coded results
- Interactive elements

You can customize the colors and styling by editing the CSS section in `app.py`.

---

## 🔧 API Endpoints

### POST `/predict`
Analyze email content for spam detection.

**Request Body:**
```json
{
  "text": "Email content to analyze"
}
```

**Response:**
```json
{
  "verdict": "SPAM" | "LEGITIMATE",
  "confidence": 0.95
}
```

---

## 📊 Performance Metrics

- **Accuracy**: 95%+
- **Response Time**: <1 second
- **Model Size**: ~250MB
- **Supported Languages**: English

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sujit Kumar**
- GitHub: [@sujitKrS04](https://github.com/sujitKrS04)
- Project: [spam_email_detection](https://github.com/sujitKrS04/spam_email_detection)

---

## 🙏 Acknowledgments

- Hugging Face for the Transformers library
- Streamlit for the amazing web framework
- FastAPI for the high-performance backend
- The open-source community

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/sujitKrS04/spam_email_detection/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

---

<div align="center">

**Made with ❤️ by Sujit Kumar**

⭐ Star this repository if you find it helpful!

</div>
