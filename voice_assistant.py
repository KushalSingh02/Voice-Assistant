import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return None

if __name__ == "__main__":
    speak("Hello! How can I help you?")
    
    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hello! How are you?")
            elif "how are you" in command:
                speak("I'm just a virtual assistant, but I'm doing great! How about you?")
            elif "what is your name" in command:
                speak("I am your voice assistant.")
            elif "who made you" in command:
                speak("I was created by Kushal Kumar Singh.")
            elif "tell me a joke" in command:
                speak("Why don't programmers like nature? Because it has too many bugs!")
            elif "exit" in command or "goodbye" in command:
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("I didn't understand that. Can you say it again?")
