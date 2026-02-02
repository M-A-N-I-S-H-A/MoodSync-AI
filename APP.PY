import streamlit as st
import brain
from datetime import datetime
import urllib.parse

# Page Config
st.set_page_config(page_title="MoodSync AI", page_icon="🎵")

st.title("🎵 MoodSync AI: Tamil Edition")
st.markdown("### How are you feeling right now?")

# Input
user_text = st.text_input("Describe your mood:", placeholder="e.g., I'm feeling so happy today!")

if st.button("Sync My Vibe"):
    if user_text:
        with st.spinner("AI is analyzing your vibe..."):
            detected_mood = brain.get_mood(user_text)
            
        if "ERROR" in detected_mood:
            st.error("Check your API Key connection!")
        else:
            st.success(f"Detected Mood: {detected_mood}")
            
            # Tamil Playlist Logic
            queries = {
                "SAD": "Tamil Sad Melodies",
                "HEART BROKEN": "Tamil Breakup Songs",
                "LOVE": "Tamil Romantic Hits",
                "ITEM": "Tamil Kuthu Songs", 
                "LONELY": "Tamil Lonely Melodies"
            }
            
            query = queries.get(detected_mood, "Latest Tamil Hits")
            encoded_query = urllib.parse.quote(query)
            spotify_url = f"https://open.spotify.com/search/{encoded_query}"
            
            # Action Buttons
            st.balloons() if detected_mood == "HAPPY" or detected_mood == "LOVE" else None
            st.link_button(f"Click to Listen to {detected_mood} Songs 🎧", spotify_url)
            
            # Save to Diary (Optional for Web)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("mood_diary.txt", "a", encoding="utf-8") as f:
                f.write(f"[{now}] {user_text} -> {detected_mood}\n")
    else:
        st.warning("Please type something first!")