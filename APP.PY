import streamlit as st
import brain
import urllib.parse

st.set_page_config(page_title="MoodSync AI", page_icon="🎵")

st.title("🎵 MoodSync AI: Tamil Edition")
st.markdown("### How are you feeling right now?")

user_text = st.text_input("Describe your mood:", placeholder="e.g., I'm feeling so happy today!")

if st.button("Sync My Vibe"):
    if user_text:
        with st.spinner("AI is analyzing your vibe..."):
            detected_mood = brain.get_mood(user_text)
            
        if "ERROR" in detected_mood:
            st.error("Check your internet connection or API Key!")
        else:
            st.success(f"Detected Mood: {detected_mood}")
            
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
            
            if detected_mood in ["LOVE", "HAPPY"]:
                st.balloons()
            st.link_button(f"Listen to {detected_mood} Songs 🎧", spotify_url)
    else:
        st.warning("Please type something first!")