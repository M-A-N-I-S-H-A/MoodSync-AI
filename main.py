import streamlit as st
import brain
import urllib.parse

st.title("🎵 MoodSync AI: Tamil Edition")
user_text = st.text_input("How are you feeling?")

if st.button("Sync My Vibe"):
    mood = brain.get_mood(user_text)
    if mood == "ERROR":
        st.error("AI connection failed. Check your Secrets!")
    else:
        st.success(f"Mood: {mood}")
        query = urllib.parse.quote(f"Tamil {mood} songs")
        st.link_button("Listen on Spotify 🎧", f"https://open.spotify.com/search/{query}")