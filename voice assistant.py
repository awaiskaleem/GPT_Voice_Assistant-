import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "your api key"

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    
    def listen(self):
        with self.microphone as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

class GPTProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def process(self, text):
        print("Processing with GPT-3.5-turbo...")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0,  # Set temperature to 0 for deterministic output
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text}
                ]
            )
            message_content = response.choices[0].message['content'].strip()
            print(f"GPT-3.5-turbo response: {message_content}")
            return message_content
        except Exception as e:
            print(f"Error processing the text: {e}")
            return None

class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def speak(self, text):
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

class MainAssistant:
    def __init__(self):
        self.voice_input = VoiceInput()
        self.processor = GPTProcessor(openai.api_key)
        self.voice_output = VoiceOutput()
    
    def run(self):
        print("Starting the assistant...")
        user_input = self.voice_input.listen()
        if user_input:
            response = self.processor.process(user_input)
            if response:
                self.voice_output.speak(response)
            else:
                self.voice_output.speak("Sorry, I couldn't process that.")
        else:
            self.voice_output.speak("Sorry, I didn't catch that.")

if __name__ == "__main__":
    assistant = MainAssistant()
    assistant.run()
