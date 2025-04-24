import streamlit as st
from transformers import pipeline
import time

# Load translation models (cached for performance)
@st.cache_resource
def load_models():
    return {
        'Hindi': pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
    }

# Language configurations with color themes
TARGET_LANGUAGES = {
    'Hindi': {'color': '#FF6B6B', 'icon': '🟥'}
}

# Gradient background function
def set_bg_gradient():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Colorful header
def colorful_header():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');
        .title-text {
            font-family: 'Poppins', sans-serif;
            font-size: 2.5rem;
            background: linear-gradient(90deg, #FF6B6B, #FFD166);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
        <h1 class="title-text">AI-Powered Translator 🌐</h1>
        """,
        unsafe_allow_html=True
    )

# Function to create colorful cards
def colorful_card(text, title, color, icon):
    return f"""
    <div style="
        background-color: {color};
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        min-height: 200px;
    ">
        <h3 style="color: white; text-align: center;">{icon} {title}</h3>
        <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 0.5rem;
            border-radius: 5px;
            min-height: 120px;
        ">
            {text}
        </div>
    </div>
    """

def main():
    # Set page config
    st.set_page_config(
        page_title="AI-Powered Translator",
        page_icon="🌐",
        layout="wide"
    )
    
    set_bg_gradient()
    colorful_header()
    
    st.markdown("""
    <div style="
        background-color: rgba(255,255,255,0.8);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        text-align: center;
    ">
        <p style="font-size: 1.1rem;">This app uses local AI models to translate English to Hindi</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load models
    with st.spinner("Loading AI models... (This happens only once)"):
        models = load_models()
    
    input_text = st.text_area(
        "Enter English text to translate:", 
        height=150,
        placeholder="Type or paste your English text here..."
    )
    
    if st.button("✨ Translate Now ✨", use_container_width=True):
        if not input_text.strip():
            st.warning("Please enter some text to translate.")
        else:
            with st.spinner("AI is translating..."):
                cols = st.columns(1)
                for i, (lang, info) in enumerate(TARGET_LANGUAGES.items()):
                    with cols[i]:
                        start_time = time.time()
                        translation = models[lang](input_text)[0]['translation_text']
                        st.markdown(
                            colorful_card(
                                translation,
                                lang,
                                info['color'],
                                info['icon']
                            ),
                            unsafe_allow_html=True
                        )
                        st.caption(f"Translated in {time.time()-start_time:.2f}s")

    st.markdown("---")
    st.markdown(f"""
    <div style="
        background-color: rgba(255,255,255,0.8);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    ">
        <p style="color: #555;">Made by SSM 🌹</p>
        <div style="display: flex; justify-content: center; gap: 10px;">
            <span style="color: {TARGET_LANGUAGES['Hindi']['color']}">Hindi {TARGET_LANGUAGES['Hindi']['icon']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
