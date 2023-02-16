from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Attachments

# Create your views here.
def chat(request,template='chat/home.html'):
    if request.user.is_authenticated:
        return redirect('chat:dashboard')
    else:
        return render(request,template)

@login_required
def dashboard(request,template='chat/dashboard.html'):
    uploads = Attachments.objects.filter(user_id=request.user.id).order_by('-uploaded_at')
    if request.method == "POST" and request.FILES['attachment']:
        file = request.FILES['attachment']
        Attachments.objects.create(attachment=file,user=request.user)
    return render(request,template,{'uploads':uploads})