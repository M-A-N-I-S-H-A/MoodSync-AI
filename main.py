import brain
import player
from datetime import datetime

def save_to_diary(user_input, mood):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{now}] Input: {user_input} | Mood: {mood}\n"
    with open("mood_diary.txt", "a", encoding="utf-8") as file:
        file.write(entry)

def run_app():
    print("\n" + "="*40)
    print("🌟 MOODSYNC AI: TAMIL EDITION 🌟")
    print("Moods: SAD, HEART BROKEN, LOVE, ITEM, LONELY")
    print("="*40)
    print("(Type 'quit' to exit)")

    while True:
        # You can now type in Tamil like "Enaku romba kavalaiya iruku"
        user_text = input("\nEpadi irukinga? (How are you feeling?) > ")

        if user_text.lower() == 'quit':
            print("Poitu varan! (Goodbye!) 👋")
            break

        if not user_text.strip():
            continue

        print("🧠 Analyzing your vibe...")
        detected_mood = brain.get_mood(user_text)

        if "ERROR" in detected_mood:
            print("❌ Error! Check your connection.")
        else:
            print(f"✨ Vibe: {detected_mood}")
            player.play_mood(detected_mood)
            save_to_diary(user_text, detected_mood)
            print("📝 Entry added to your Tamil Mood Diary.")

if __name__ == "__main__":
    run_app()