# 🛡️ Spam Sentinel AI

AI-powered SMS Spam Detection system built using Machine Learning and Streamlit.

## 🚀 Features
- Detects spam and phishing SMS
- NLP preprocessing with NLTK
- TF-IDF vectorization
- Real-time predictions via Streamlit UI

## 🧠 Tech Stack
- Python
- Streamlit
- Scikit-learn
- NLTK

## 📊 Model Training
Training code and dataset are available in the `training/` folder.
The deployed app uses pre-trained artifacts (`model.pkl`, `vectorizer.pkl`).

## ▶️ Run Locally
```bash
pip install streamlit nltk scikit-learn
streamlit run app.py
