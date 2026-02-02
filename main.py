import customtkinter as ctk
import brain
import player
from datetime import datetime

# Basic App Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MoodSyncApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("MoodSync AI - Music Edition")
        self.geometry("500x450")

        # Header
        self.label = ctk.CTkLabel(self, text="MoodSync AI", font=("Helvetica", 26, "bold"))
        self.label.pack(pady=30)

        # Input Box
        self.entry = ctk.CTkEntry(self, placeholder_text="Tell me how you feel...", width=380, height=45)
        self.entry.pack(pady=10)

        # Action Button
        self.button = ctk.CTkButton(self, text="Sync My Music 🎵", font=("Helvetica", 14, "bold"), height=40, command=self.process_mood)
        self.button.pack(pady=20)

        # Result Display
        self.result_label = ctk.CTkLabel(self, text="", font=("Helvetica", 18))
        self.result_label.pack(pady=10)

        # Status Display
        self.status_label = ctk.CTkLabel(self, text="", font=("Helvetica", 12), text_color="gray")
        self.status_label.pack(pady=5)

    def save_to_diary(self, user_input, mood):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{now}] Input: {user_input} | Mood: {mood}\n"
        with open("mood_diary.txt", "a", encoding="utf-8") as file:
            file.write(entry)

    def process_mood(self):
        user_text = self.entry.get()
        if not user_text.strip():
            return

        self.result_label.configure(text="Analyzing...", text_color="white")
        self.update_idletasks()

        # Get the mood from Gemini (brain.py)
        detected_mood = brain.get_mood(user_text)

        if "ERROR" in detected_mood:
            self.result_label.configure(text="Connection Error!", text_color="red")
        else:
            self.result_label.configure(text=f"Mood: {detected_mood}", text_color="#1DB954")
            
            # This plays the Tamil songs via player.py
            player.play_mood(detected_mood)
            
            # Save the record
            self.save_to_diary(user_text, detected_mood)
            self.status_label.configure(text="Diary updated successfully.")
            
            # Reset input field
            self.entry.delete(0, 'end')

if __name__ == "__main__":
    app = MoodSyncApp()
    app.mainloop()