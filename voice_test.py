from gtts import gTTS
from playsound import playsound

tts = gTTS("Hello, I am speaking.")
tts.save("test.mp3")

playsound("test.mp3")
