import streamlit as st
import brain
import urllib.parse

# Page Setup
st.set_page_config(page_title="MoodSync AI", page_icon="🎵")
st.title("🎵 MoodSync AI: Tamil Edition")
st.markdown("### How are you feeling right now?")

# Input
user_text = st.text_input("Describe your mood:", placeholder="e.g., Today was such a tiring but good day...")

if st.button("Sync My Vibe"):
    if user_text:
        with st.spinner("AI is analyzing your vibe..."):
            detected_mood = brain.get_mood(user_text)
            
        if "ERROR" in detected_mood:
            st.error("AI connection failed. Check your Gemini API Key in Settings -> Secrets!")
        else:
            st.success(f"Detected Mood: {detected_mood}")
            
            # Search logic
            query = urllib.parse.quote(f"Tamil {detected_mood} songs")
            spotify_url = f"https://open.spotify.com/search/{query}"
            
            if detected_mood in ["LOVE", "HAPPY"]:
                st.balloons()
            
            st.link_button(f"Click to Listen to {detected_mood} Songs 🎧", spotify_url)
    else:
        st.warning("Please type something first!")