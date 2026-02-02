import google.genai as genai

# HARDCODED KEY FOR TESTING
client = genai.Client(api_key="AIzaSyBNxO5PtbuOcWwsj8_LJuICxfgPb3-VR30")

def get_mood(user_text):
    try:
        model_id = "gemini-2.0-flash"
        prompt = f"Analyze the mood of this text: '{user_text}'. Return ONLY one word: SAD, LOVE, HAPPY, ITEM, or LONELY."
        
        response = client.models.generate_content(model=model_id, contents=prompt)
        return response.text.strip().upper()
    except Exception as e:
        # This will show the real error message if it fails
        return f"ERROR: {str(e)}"