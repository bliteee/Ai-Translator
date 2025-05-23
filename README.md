# Ai-Translator

# 🌈 AI Text Translator Web App

A colorful web application that translates English text to Hindi, built with Streamlit.

🖥 Try it here →[Link for website](https://ai-translator-shshshnk.streamlit.app/)

## ✨ Features

- **Colorful UI**: Visually appealing design with themed language cards
- **Real-time Translation**: Instant results with loading indicators
- **Responsive Design**: Works on both desktop and mobile devices

## 🛠️ Technologies Used

- Python 3.9+
- Streamlit (UI)
- Hugging Face Transformers (AI models)
- PyTorch (ML backend)

## 🧠 Model Information
- Hindi: Helsinki-NLP/opus-mt-en-hi (~200MB)

## ⚠️ Known Issues
- First-time load takes 1-2 minutes (model download)
- Long texts (>100 words) may take 5-10 seconds

## 📂 Project Structure
```bash
- ai-text-translator/  
├── translator_app.py       # Main application code  
├── requirements.txt        # Dependencies  
└── README.md              # This documentation  

