import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Language codes for our target languages with color themes
TARGET_LANGUAGES = {
    'Hindi': {'code': 'hi', 'color': '#FF6B6B', 'icon': '🛑'},
    'Gujarati': {'code': 'gu', 'color': '#FFD166', 'icon': '🛑'}
}

# Function to perform translation
def translate_text(text, dest_language):
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Error in translation: {str(e)}"

# Gradient background function
def set_bg_gradient():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}
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
        <h1 class="title-text">AI Text Translator 🌐</h1>
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

# Main app function
def main():
    # Set page config
    st.set_page_config(
        page_title="AI Text Translator",
        page_icon="🌐",
        layout="wide"
    )
    
    # Set gradient background
    set_bg_gradient()
    
    # Add colorful header
    colorful_header()
    
    # Description
    st.markdown("""
    <div style="
        background-color: rgba(255,255,255,0.8);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        text-align: center;
    ">
        <p style="font-size: 1.1rem;">This app instantly translates English text to Hindi and Gujarati using Google Translate API.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input text area with colorful border
    input_text = st.text_area(
        "Enter English text to translate:", 
        height=150,
        placeholder="Type or paste your English text here...",
        help="The text you enter here will be translated to both languages"
    )
    
    # Colorful translate button
    if st.button(
        "✨ Translate Now ✨",
        use_container_width=True,
        help="Click to translate your text"
    ):
        if not input_text.strip():
            st.warning("Please enter some text to translate.")
        else:
            with st.spinner("Translating your text..."):
                # Create columns for translations
                cols = st.columns(2)
                
                for i, (lang, info) in enumerate(TARGET_LANGUAGES.items()):
                    with cols[i]:
                        translated_text = translate_text(input_text, info['code'])
                        st.markdown(
                            colorful_card(
                                translated_text,
                                lang,
                                info['color'],
                                info['icon']
                            ),
                            unsafe_allow_html=True
                        )
                st.session_state.translated = True
    
    # Add some animated confetti on successful translation
    if st.session_state.get('translated', False):
        st.balloons()
        st.session_state.translated = False  # Reset after showing
    
    # Footer with colorful accents
    st.markdown("---")
    st.markdown(f"""
    <div style="
        background-color: rgba(255,255,255,0.8);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    ">
        <p style="color: #555;">Made SSM ❤️</p>
        <div style="display: flex; justify-content: center; gap: 10px;">
            <span style="color: {TARGET_LANGUAGES['Hindi']['color']}">Hindi {TARGET_LANGUAGES['Hindi']['icon']}</span>
            <span style="color: {TARGET_LANGUAGES['Gujarati']['color']}">Gujarati {TARGET_LANGUAGES['Gujarati']['icon']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    if 'translated' not in st.session_state:
        st.session_state.translated = False
    main()