import pyttsx3
def text_to_speach(text):

    engine = pyttsx3.init()
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)  
    engine.setProperty('volume', 1)  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
