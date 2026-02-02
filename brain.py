import google.genai as genai

# PASTE YOUR ACTUAL KEY INSIDE THESE QUOTES
client = genai.Client(api_key="AIzaSyBNxO5PtbuOcWwsj8_LJuICxfgPb3-VR30") 

def get_mood(user_text):
    try:
        model_id = "gemini-2.0-flash"
        prompt = f"""
        Analyze the emotional vibe of this text: "{user_text}"
        Return ONLY one of these exact words: SAD, HEART BROKEN, LOVE, ITEM, or LONELY.
        """
        response = client.models.generate_content(model=model_id, contents=prompt)
        return response.text.strip().upper()
    except Exception as e:
        return f"ERROR: {str(e)}"