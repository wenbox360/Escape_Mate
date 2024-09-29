import speech_recognition as sr
import sounddevice
import asyncio

# Define the code word to detect
CODE_WORD = "escape mate"


# Initialize recognizer class
recognizer = sr.Recognizer()
recognizer.energy_threshold = 400


# Use microphone as the audio input
async def recognize_speech(question_queue):
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        print("Ready to receive voice input...")  # Debug print
        
        # Continuous loop to keep listening for input
        while True:
            try:
                # Listen for the audio input in a non-blocking way
                print("Listening for speech...")
                # Move the blocking listen call to a thread-safe context
                audio = await asyncio.to_thread(recognizer.listen, source)

                # Recognize speech in a thread-safe way
                text = await asyncio.to_thread(recognizer.recognize_google, audio)
                print(f"Recognized text: {text}")  # Debug print

                # Check if the code word is present anywhere in the recognized sentence
                if CODE_WORD.lower() in text.lower():
                    print(f"Code word detected: {text}")
                    await question_queue.put(text)

            except sr.UnknownValueError:
                # If speech is unintelligible
                print("Sorry, I could not understand. Could you say that again?")
            except sr.RequestError as e:
                # If there's a request error with the recognition service
                print(f"Could not request results; {e}")

            # Allow the loop to be non-blocking
            await asyncio.sleep(0.1)  # Adjust as necessary for responsiveness
