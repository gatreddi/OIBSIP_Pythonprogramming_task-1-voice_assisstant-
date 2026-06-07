import tkinter as tk
from tkinter import scrolledtext
import datetime
import pyjokes
import pywhatkit
import webbrowser
from gtts import gTTS
from playsound import playsound
import os


# Voice Function
def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("voice.mp3")
        playsound("voice.mp3")

        if os.path.exists("voice.mp3"):
            os.remove("voice.mp3")

    except:
        pass


# Assistant Logic
def process_command():

    command = entry.get().lower().strip()

    chat.insert(tk.END, f"\nYou: {command}\n")

    response = ""

    if command in ["hello", "hi", "hey"]:
        response = "Hello! How can I help you?"

    elif "time" in command:
        response = datetime.datetime.now().strftime(
            "Current time is %I:%M %p"
        )

    elif "date" in command:
        response = datetime.datetime.now().strftime(
            "Today's date is %d %B %Y"
        )

    elif "joke" in command:
        response = pyjokes.get_joke()

    elif "open google" in command:
        response = "Opening Google"
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        response = "Opening YouTube"
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        response = "Opening Gmail"
        webbrowser.open("https://mail.google.com")

    elif command.startswith("play"):
        song = command.replace("play", "").strip()

        if song:
            response = f"Playing {song}"
            pywhatkit.playonyt(song)
        else:
            response = "Please enter a song name"

    elif "your name" in command:
        response = "My name is James. I am your voice assistant."

    elif command in ["exit", "bye", "quit"]:
        root.destroy()
        return

    else:
        response = "Sorry, I did not understand."

    chat.insert(tk.END, f"Assistant: {response}\n")
    chat.see(tk.END)

    speak(response)

    entry.delete(0, tk.END)


# GUI Window
root = tk.Tk()
root.title("James Voice Assistant")
root.geometry("600x500")

title = tk.Label(
    root,
    text="🤖 James Voice Assistant",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

chat = scrolledtext.ScrolledText(
    root,
    width=70,
    height=20
)
chat.pack(pady=10)

entry = tk.Entry(
    root,
    width=50,
    font=("Arial", 12)
)
entry.pack(pady=10)

send_btn = tk.Button(
    root,
    text="Send",
    command=process_command,
    font=("Arial", 12)
)
send_btn.pack()

chat.insert(
    tk.END,
    "Assistant: Hello! I am James. Type a command below.\n"
)

root.mainloop()