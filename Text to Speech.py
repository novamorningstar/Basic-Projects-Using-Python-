from gtts import gTTS
from playsound import playsound
text = "I don't know" #Enter the text you want to convert 
language = "en" #the language you want to convert to
obj = gTTS(text=text, lang=language, slow=False)
obj.save("filename.mp3")
playsound("filename.mp3")