import text_to_speach
import speachToText
import webbrowser

user_data=speachToText.voice_to_text()
print(user_data)
if "what is your name" in user_data:
    text_to_speach.text_to_speach("My name is lili,sir")
elif "hello" in user_data:
    text_to_speach.text_to_speach("hey sir")
elif "shutdown" in user_data:
    text_to_speach.text_to_speach("ok,sir")
elif "play song" in  user_data:
    text_to_speach.text_to_speach("playing song")
    webbrowser.open("https://youtube.com")
    
else:
    text_to_speach.text_to_speach("I am unable sir")

