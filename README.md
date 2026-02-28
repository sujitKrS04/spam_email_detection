# 🛡️ SmartCastAI - Advanced Email Security & Threat Detection

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**SmartCastAI** is an end-to-end machine learning application designed to identify spam email content with high precision. The system uses a fine-tuned **DistilBERT Transformer model** for advanced natural language understanding and real-time spam detection.

</div>

---

## ✨ Features

- 🎯 **High Accuracy Detection** - Powered by fine-tuned DistilBERT transformer model
- ⚡ **Real-time Analysis** - Instant threat detection and classification
- 🎨 **Clean UI** - Simple, professional interface with intuitive design
- 📊 **Confidence Scoring** - Detailed probability metrics for each prediction
- 🔍 **Email Statistics** - Character count, word count, and risk level analysis
- 🧪 **Sample Testing** - Pre-loaded example emails for quick testing
- 🔒 **Enterprise-Grade** - Production-ready API with FastAPI backend
- 🧠 **Transformer Architecture** - Advanced NLP using DistilBERT

---

## 🖼️ Interface Preview

The application features a clean, modern interface with:

- **Simple, professional design** with blue action buttons
- **Color-coded result cards** (red for spam, green for safe)
- **Confidence score display** with percentage metrics
- **Email statistics** including character count, word count, and risk level
- **Sidebar navigation** with sample emails for quick testing
- **Responsive design** that works on all screen sizes

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Dependencies

The project uses the following key dependencies (see [requirements.txt](requirements.txt) for full list):

- **streamlit** (≥1.28.0) - Web interface framework
- **fastapi** (≥0.100.0) - Backend API framework
- **uvicorn** (≥0.23.0) - ASGI server
- **transformers** (≥4.30.0) - Hugging Face transformers library
- **torch** (≥2.0.0) - PyTorch for model inference
- **requests** (≥2.31.0) - HTTP library for API calls
- **safetensors** (≥0.3.0) - Safe model serialization format

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/sujitKrS04/spam_email_detection.git
   cd spam_email_detection
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the model is available**

   The application uses a fine-tuned DistilBERT model stored in the `smartcast_bert_model/` directory. This folder should contain:
   - `config.json`
   - `model.safetensors`
   - `tokenizer.json`
   - `tokenizer_config.json`

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

### Verifying the Setup

To verify everything is working correctly:

1. **Check API is running**: Visit `http://127.0.0.1:8000/docs` in your browser to see the FastAPI interactive documentation
2. **Test the endpoint**: Use the FastAPI docs to send a test request
3. **Open Streamlit**: Access `http://localhost:8501` and try the sample emails

---

## 📖 Usage Guide

### Using the Web Interface

1. **Open the application** in your browser (usually `http://localhost:8501`)
2. **Enter email content** in the text area, or select a sample from the sidebar:
   - **Suspicious Email**: Contains urgent language and suspicious links
   - **Legitimate Email**: Professional business communication
   - **Phishing Attempt**: Attempts to steal credentials with fake links
3. **Click "Analyze Email"** to start the analysis
4. **View the results** including:
   - Threat classification (SPAM or LEGITIMATE)
   - Confidence score percentage
   - Basic email statistics (character count, word count)
   - Risk level assessment

### Using the API Directly

You can also use the FastAPI backend directly:

```python
import requests

API_URL = "http://127.0.0.1:8000/predict"

response = requests.post(API_URL, json={
    "text": "Your email content here"
})

result = response.json()
print(f"Is Spam: {result['is_spam']}")
print(f"Verdict: {result['verdict']}")
print(f"Confidence: {result['confidence']}")
```

### Testing with Client Script

Run the automated counterfactual testing to see how the model responds to systematic variations:

```bash
python client.py
```

This script performs **counterfactual security testing** by:

- Starting with a base suspicious email
- Systematically removing features (urgent keywords, links, suspicious words)
- Testing each variation against the API
- Showing how model confidence changes with each modification

This helps understand which features the model considers most important for spam detection.

---

## 🏗️ Project Structure

```
spam_email_detection/
├── app.py                          # Streamlit frontend application
├── main.py                         # FastAPI backend server
├── client.py                       # Automated testing script
├── requirements.txt                # Python dependencies
├── smartcast_bert_model/           # Fine-tuned DistilBERT model
│   ├── config.json
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   └── model.safetensors          # (Not in repo - too large)
├── README.md                       # This file
└── LICENSE                         # MIT License
```

---

## 🧠 Model Architecture

### Technology Stack

- **Base Model**: DistilBERT (distilbert-base-uncased)
- **Task**: Binary Sequence Classification
- **Framework**: Hugging Face Transformers + PyTorch
- **Backend**: FastAPI for high-performance API
- **Frontend**: Streamlit with custom CSS
- **Tokenizer**: DistilBertTokenizerFast

### Model Details

- **Architecture**: DistilBertForSequenceClassification
- **Input**: Text sequences (max 512 tokens)
- **Output**: Binary classification with confidence scores
- **Inference Mode**: torch.no_grad() for optimal performance
- **Softmax activation** for probability distribution
- **Model Location**: `./smartcast_bert_model/`

---

## 🎨 UI Customization

The interface uses custom CSS with:

- Clean, professional styling
- Blue action buttons (#4A90E2)
- Card-based result displays (green for safe, red for spam)
- Gray metric cards for statistics
- Responsive layout
- Interactive elements

You can customize the colors and styling by editing the CSS section in [app.py](app.py).

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
  "is_spam": true,
  "verdict": "SPAM",
  "confidence": 0.95
}
```

**Response Fields:**

- `is_spam` (boolean): True if email is classified as spam, False otherwise
- `verdict` (string): "SPAM" or "LEGITIMATE"
- `confidence` (float): Confidence score between 0 and 1

---

## 📊 Performance Metrics

- **Model**: Fine-tuned DistilBERT (distilbert-base-uncased)
- **Response Time**: < 1 second for inference
- **Model Size**: ~250MB
- **Max Input Length**: 512 tokens
- **Supported Languages**: English

---

## 🔧 Troubleshooting

### Common Issues

**1. "Could not connect to the API" error**

- Ensure the FastAPI server is running on port 8000
- Check if the correct URL is used: `http://127.0.0.1:8000`
- Verify no firewall is blocking the connection

**2. "ModuleNotFoundError" or import errors**

- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.8 or higher
- Check if all dependencies are installed correctly

**3. Model loading errors**

- Verify `smartcast_bert_model/` directory exists
- Ensure all required files are present:
  - `config.json`
  - `model.safetensors`
  - `tokenizer.json`
  - `tokenizer_config.json`

**4. Port already in use**

- Change the port in the uvicorn command: `--port 8001`
- Update the API_URL in `app.py` accordingly

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
