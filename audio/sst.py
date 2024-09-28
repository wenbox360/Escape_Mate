import speech_recognition as sr
import sounddevice

# Define the code word to detect
CODE_WORD = "shadow"

# Initialize recognizer class
recognizer = sr.Recognizer()

# Use microphone as the audio input
with sr.Microphone() as source:
    #Adjusting for ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
    
    while True:
        try:
            # Listen for the audio input
            audio = recognizer.listen(source)
            
            # Convert the audio to text using Google's speech recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Check if the code word is present anywhere in the recognized sentence
            if CODE_WORD.lower() in text.lower():
                # If the code word is detected do something
                print("Code word detected!") # Placeholder for the action to be taken
        except sr.UnknownValueError:
            # If speech is unintelligible
            print("Sorry, I could not understand. Please try again.") # Placeholder for the action to be taken
        except sr.RequestError as e:
            # If there's a request error with the recognition service
            print(f"Could not request results; {e}")
