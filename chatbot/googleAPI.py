import google.generativeai as genai

#List of Models
#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

#Generate Content
#response = model.generate_content("What is the meaning of life?")
#print(response.text)

#Chat
# history = [
#     {
#         "parts": {
#             'text': "In one sentence, explain how a computer works to a young child."
#         },
#         "role": "user"
#     },
#     {
#         "parts": {
#             'text': "A computer is like a very smart machine that can understand and follow our instructions, help us with our work, and even play games with us!"
#         },
#         "role": "model"
#     }
# ]

def ask_Google(message, image, history):
    genai.configure(api_key='AIzaSyAnHBcdEczO7mFg9xKeuoK3bZg-XAR9W9Q')
    model = genai.GenerativeModel('gemini-pro')

    chat = model.start_chat(history=history)
    response = chat.send_message(content=[message, image])
    return response.text

#for message in chat.history:
#    print(f'**{message.role}**: {message.parts[0].text}')