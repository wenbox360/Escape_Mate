import speech_recognition as sr
import sounddevice


# Define the code word to detect
CODE_WORD = "shadow"


# Initialize recognizer class
recognizer = sr.Recognizer()
recognizer.energy_threshold = 400


# Use microphone as the audio input
def recognize_speech():
           with sr.Microphone() as source:
               #Adjusting for ambient noise
               recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
               try:
                   # Listen for the audio input
                   audio = recognizer.listen(source)
                  
                   # Convert the audio to text using Google's speech recognition
                   text = recognizer.recognize_google(audio)
                   command = ""
                   # Check if the code word is present anywhere in the recognized sentence
                   if text.split()[0].lower() == CODE_WORD.lower():
                       # Placeholder for the action to be taken
                       print(f"You said: {text}")
                       command = text
               except sr.UnknownValueError:
                   # If speech is unintelligible
                   print("Sorry, I could not understand. Could you say that again?") # Placeholder for the action to be taken
               except sr.RequestError as e:
                   # If there's a request error with the recognition service
                   print(f"Could not request results; {e}")
               #return command
               return command


# Main function
if __name__ == "__main__":
   recognize_speech() 

