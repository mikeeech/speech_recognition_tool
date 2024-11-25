import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print('Listening...')
        audio = recognizer.listen(source)
        try:
            speech_text = recognizer.recognize_google(audio)
            print(f'Recognized text: {speech_text}')

            speak(speech_text)

        except sr.UnknownValueError:
            print(f"Sorry, I didn't catch that")
        except sr.RequestError as e:
            print(f'There has been a request error: {e}')
