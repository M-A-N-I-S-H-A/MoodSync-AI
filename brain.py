import google.genai as genai
import streamlit as st

# This line links your code to the 'Secrets' you saved in the screenshot
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def get_mood(user_text):
    try:
        # Using the standard stable model ID
        model_id = "gemini-2.0-flash"
        
        prompt = f"""
        Analyze the emotional vibe of this text: "{user_text}"
        Return ONLY one of these exact words: SAD, HEART BROKEN, LOVE, ITEM, or LONELY.
        """
        
        response = client.models.generate_content(model=model_id, contents=prompt)
        return response.text.strip().upper()
    except Exception as e:
        return "ERROR"