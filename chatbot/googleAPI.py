import google.generativeai as genai
from pathlib import Path
import os

#List of Models
#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

google_api_key = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=google_api_key)

def ask_Google(messages):
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(messages)

    return response.text

def ask_GoogleImage(message, image):
    model = genai.GenerativeModel('gemini-pro-vision')

    file_directory = 'chatbot/userfiles'
    os.makedirs(file_directory, exist_ok=True)
    image_path = os.path.join(file_directory, image.name)

    with open(image_path, 'wb') as file:
        file.write(image.read())

    picture = [{
        'mime_type': 'image/jpeg',
        'data': Path(image_path).read_bytes()
    }]

    prompt = [message, picture[0]]

    response = model.generate_content(
        contents=prompt)

    return response.text

#for message in chat.history:
#    print(f'**{message.role}**: {message.parts[0].text}')