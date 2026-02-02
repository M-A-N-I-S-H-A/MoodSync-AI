import streamlit as st
import brain
import os
from datetime import datetime
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="MoodSync AI", page_icon="🎵")

# 2. Styling
st.title("🎵 MoodSync AI: Tamil Edition")
st.markdown("### How are you feeling right now?")

# 3. User Input
user_text = st.text_input("Describe your mood:", placeholder="e.g., Today was such a tiring but good day...")

# 4. Logic
if st.button("Sync My Vibe"):
    if user_text:
        with st.spinner("AI is analyzing your vibe..."):
            # This calls your brain.py file
            detected_mood = brain.get_mood(user_text)
            
        if "ERROR" in detected_mood:
            st.error("Check your Gemini API Key in the Settings -> Secrets!")
        else:
            st.success(f"Detected Mood: {detected_mood}")
            
            # Tamil Playlist Search Terms
            queries = {
                "SAD": "Tamil Sad Melodies",
                "HEART BROKEN": "Tamil Breakup Songs Love Failure",
                "LOVE": "Tamil Romantic Hits Melody",
                "ITEM": "Tamil Item Songs Kuthu Songs", 
                "LONELY": "Tamil Lonely Melodies Midnight Mix"
            }
            
            query = queries.get(detected_mood, "Latest Tamil Hits 2026")
            encoded_query = urllib.parse.quote(query)
            spotify_url = f"https://open.spotify.com/search/{encoded_query}"
            
            # Interaction
            if detected_mood in ["LOVE", "HAPPY"]:
                st.balloons()
            
            st.link_button(f"Click to Listen to {detected_mood} Songs 🎧", spotify_url)
            
            # Save to a local diary file on the server (Optional)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("mood_diary.txt", "a", encoding="utf-8") as f:
                f.write(f"[{now}] {user_text} -> {detected_mood}\n")
    else:
        st.warning("Please type something first!")