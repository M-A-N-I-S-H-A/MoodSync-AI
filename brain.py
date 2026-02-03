import google.genai as genai

# Setup - Paste your Gemini API Key here
client = genai.Client(api_key="AIzaSyAJz0oHSeh8rij816taZF_4DSW3EJDdxGU")

def get_mood(user_text):
    try:
        model_id = "gemini-2.5-flash"
        
        # Updated prompt with your custom mood categories
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

if __name__ == "__main__":
    # Test your new moods
    print(f"Test Mood: {get_mood('I am so in love with this music!')}")