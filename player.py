import webbrowser
import urllib.parse

def play_mood(mood):
    # Mapping moods to SPECIFIC TAMIL search terms
    queries = {
        "SAD": "Tamil Sad Melodies",
        "HEART BROKEN": "Tamil Breakup Songs Love Failure",
        "LOVE": "Tamil Romantic Hits Melody",
        "ITEM": "Tamil Item Songs Kuthu Songs", # High energy Kuthu/Dance
        "LONELY": "Tamil Lonely Melodies Midnight Mix"
    }

    # Default to latest Tamil hits if mood is unrecognized
    mood_query = queries.get(mood, "Latest Tamil Hits 2026")
    encoded_query = urllib.parse.quote(mood_query)
    
    # Direct search link to Spotify
    url = f"https://open.spotify.com/search/{encoded_query}"

    print(f"--- 🎵 Playing Tamil vibes for: {mood} ---")
    webbrowser.open(url)