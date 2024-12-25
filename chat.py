import os
import google.generativeai as genai
from dotenv import load_dotenv
from text_to_speech import text_to_speech

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="You are a career guidance advisor specializing in helping university students navigate their career paths. Your role is to provide personalized advice on career planning, job opportunities, internships, skill development, and interview preparation. You are empathetic, encouraging, and resourceful, offering actionable tips and insights to help students achieve their professional goals. Your guidance should be tailored to each student’s field of study, interests, and aspirations, emphasizing practical steps for success in their desired career paths.",
)

history = []

chat_session = model.start_chat(
        history = history
    )

hello_prompt = chat_session.send_message('Hello')

hello_response = hello_prompt.text

print(f'Bot: {hello_response}')
text_to_speech(hello_response)
print('\n')

print("If you want to exit press 'Y' to exit")

while True:

    user_input = input("You: ")
    
    print('\n')

    if user_input.lower == 'y':
        user_input = input("type 'confirm' to exit: ")

        if user_input.lower == 'confirm':
            break
        
    else:
        
        response = chat_session.send_message(user_input)
    
        model_response = response.text

        print(f'Bot: {model_response}')
        text_to_speech(model_response)
        print('\n')

        chat_session.history.append({"role": "user", "parts": [user_input]})
        chat_session.history.append({"role": "model", "parts": [model_response]})