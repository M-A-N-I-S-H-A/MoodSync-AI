import google.genai as genai
import streamlit as st

# This line tells the app: "Go to Streamlit's Secret vault and grab the key"
api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

def get_mood(user_text):
    try:
        # Note: Use "gemini-2.0-flash" as the standard stable ID
        model_id = "gemini-2.0-flash"
        
        prompt = f"""
        Analyze the emotional vibe of this text: "{user_text}"
        Return ONLY one of these exact words: 
        - SAD
        - HEART BROKEN
        - LOVE
        - ITEM
        - LONELY
        """
        
        response = client.models.generate_content(model=model_id, contents=prompt)
        return response.text.strip().upper()
    except Exception as e:
        return "ERROR"