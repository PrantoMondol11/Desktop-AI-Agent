import speech_recognition as sr

# Initialize the recognizer
def voice_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        # Adjust for ambient noise to improve accuracy
        r.adjust_for_ambient_noise(source, duration=1)
        # Listen to the audio input
        audio = r.listen(source)
    
    try:
        # Recognize speech using Google's Web Speech API
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return text

