from django.shortcuts import render, redirect
from django.http import JsonResponse
from .openAIAPI import ask_openai
from .googleAPI import ask_Google

from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Chat
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user).order_by('-created_at')
    chatHistory = chats[:3]

    if request.method == 'POST':
        history = []
        for chat in chatHistory:
            usermessage = {
                "parts": {
                    'text': chat.message
                },
                "role": "user"
            }
            modelmessage = {
                "parts": {
                    'text': chat.response
                },
                "role": "model"
            }
            history.append(usermessage)
            history.append(modelmessage)

        message = request.POST.get('message')
        image2 = request.POST.get('image')
        image = request.FILES.get('image')
        print(request.FILES)
        print(image)
        print(message)
        print(image2)
        #response = ask_openai(message)
        response = "holi"#ask_Google(message, image, history)
        
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'response': response})
    return render(request, 'chatbot.html', {'chats': chats})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating the account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def clear(request):
    Chat.objects.filter(user=request.user).delete()
    return redirect('chatbot')