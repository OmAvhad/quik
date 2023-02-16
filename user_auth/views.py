from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password

# Create your views here.
@csrf_protect
def register(request,template_name="auth/register.html"):
    if request.method == "POST":
        postdata = request.POST
        serializer = RegisterSerializer(data=postdata)
        if serializer.is_valid():
            try:
                user = User.objects.filter(Q(username=postdata['username']) | Q(email=postdata['email'])).count()
            except:
                user = None
            if not user:
                user = User.objects.create(username=postdata['username'],password=make_password(postdata['password']),email=postdata['email'],first_name=postdata['name'])
                login(request,user)
                messages.success(request, "Registered Successfully" )
                return redirect('chat:dashboard')
            else:
                messages.error(request, "Email already Exists.")
        else:
            field_names = []
            for field_name, field_errors in serializer.errors.items():
                print(field_name, field_errors)
            field_names.append(field_name)
            message = f'Invalid data in {field_names}'
            messages.error(request, message )
    return render(request,template_name)

@csrf_protect
def user_login(request,template_name="auth/login.html"):
    if request.method == "POST":
        try:
            postdata = request.POST
            username = postdata['username']
            password = postdata['password']
            try:
                user = authenticate(username=username, password=password)
            except:
                user = None
            if user is not None:
                login(request,user)
                messages.success(request, "Logged In" )
                return redirect('chat:dashboard')
            else:
                messages.error(request, "User not found")
        except Exception as e:
            messages.error(request, "Some Error Occured")
    return render(request,template_name)


def logout_url(request):
    logout(request)
    messages.success(request, "Logged Out" )
    return redirect('chat:home')
