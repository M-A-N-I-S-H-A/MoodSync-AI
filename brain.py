import google.genai as genai
import streamlit as st

# This grabs the key from the "Secrets" box in your screenshot
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def get_mood(user_text):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Return only one word (SAD, HAPPY, LOVE, ITEM, or LONELY) for: {user_text}"
        )
        return response.text.strip().upper()
    except:
        return "ERROR"