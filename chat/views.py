from django.shortcuts import render

# Create your views here.
def chat(request,template='chat/chat.html'):
    return render(request,template)