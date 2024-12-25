import pyttsx3
import re

def text_to_speech(text):
    # Remove unwanted punctuation marks
    cleaned_text = re.sub(r'[^\w\s.,!?]', '', text)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for different voices

    # Convert text to speech
    engine.say(cleaned_text)
    engine.runAndWait()
    