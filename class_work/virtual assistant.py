import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
engine=pyttsx3.init()
def speak(text):
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
        try:
            command=recognizer.recognize_google(audio,language='en-in')
            print("You said:", command)
            return command.lower()
        except sr.UnknownValuesError:
            print("sorry, I did not understand.")
            speak("sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("speech service error.")
            speak("sorry, my speech service is down.")
            return ""
def run_assistant():
            speak("Hello! I'm your virtual assistant. How can I help you?")
            while True:
                command=listen()
                if 'time' in command:
                   now = datetime.datetime.now().strftime("%I:%M %p")
                   speak(f"The time is {now}")
                elif 'date'in command:
                    today = datetime.date.today().strftime("%B %d, %Y")
                    speak(f"Today's date is {today}")
                elif 'open google' in command:
                    speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                elif 'your name' in command:
                    speak("I am your python assistant!")
                elif 'stop' in command or 'exit' in command or 'bye' in command:
                    speak("okay bye bye! have a good day")
                    break
                else:
                    speak("sorry, i can't do that yet.")
run_assistant()