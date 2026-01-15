import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

st.set_page_config(page_title="Spam Sentinel AI", page_icon="🛡️", layout="centered")

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_msg(message):
    message = message.lower()
    message = nltk.word_tokenize(message)
    y = [i for i in message if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y = [ps.stem(i) for i in y]
    return " ".join(y)

#  LOADING MODELS 
@st.cache_resource 
def load_models():
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
    return tfidf, model

tfidf, model = load_models()

#  ADVANCED CYBER-TECH CSS 
st.markdown("""
    <style>
    /* Background Image with Overlay */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Glassmorphism Card Effect */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    /* Title Styling */
    h1 {
        color: #00f2fe;
        text-shadow: 0px 0px 15px #00f2fe;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Custom Text Area */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.5) !important;
        color: #00ffcc !important;
        border: 1px solid #00f2fe !important;
        border-radius: 12px;
        font-size: 16px;
    }

    /* Analyze Button 3D Effect */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        border: none;
        color: white;
        padding: 15px 32px;
        font-weight: bold;
        border-radius: 12px;
        transition: 0.4s;
        box-shadow: 0px 4px 15px rgba(0, 242, 254, 0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 25px rgba(0, 242, 254, 0.6);
        color: white;
    }

    /* Result Boxes */
    .result-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
        animation: fadeIn 1s;
    }
    .spam { 
        background: rgba(255, 75, 75, 0.2); 
        border: 2px solid #ff4b4b; 
        color: #ff4b4b; 
        text-shadow: 0px 0px 10px #ff4b4b;
    }
    .ham { 
        background: rgba(40, 167, 69, 0.2); 
        border: 2px solid #28a745; 
        color: #28a745; 
        text-shadow: 0px 0px 10px #28a745;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# Wrapping everything in a div for potential CSS targeting
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.title("🛡️ SPAM SENTINEL AI")
st.markdown("<p style='text-align:center; color:#888;'>Advanced Machine Learning for SMS Threat Detection</p>", unsafe_allow_html=True)
st.write("---")

input_sms = st.text_area("DEPLOY MESSAGE DATA:", placeholder="Paste your SMS here for neural analysis...", height=150)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_btn = st.button('🚀 RUN ANALYSIS')

if predict_btn:
    if input_sms.strip() == "":
        st.warning("Input required for analysis.")
    else:
        with st.spinner('Neural Network processing...'):
            transformed_sms = transform_msg(input_sms)
            vector_input = tfidf.transform([transformed_sms])
            result = model.predict(vector_input)[0]

        if result == 1:
            st.markdown('''
                <div class="result-box spam">
                    <h2 style="margin:0;">🚨 THREAT DETECTED</h2>
                    <p>Classification: MALICIOUS SPAM</p>
                </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown('''
                <div class="result-box ham">
                    <h2 style="margin:0;">✅ SYSTEM SECURE</h2>
                    <p>Classification: LEGITIMATE MESSAGE</p>
                </div>
            ''', unsafe_allow_html=True)
            st.balloons()

st.markdown('</div>', unsafe_allow_html=True)


st.markdown("<br><p style='text-align: center; color: #555; font-size:12px;'>ENCRYPTED ANALYTICS CORE v2.0 | IDS PROJECT</p>", unsafe_allow_html=True)