from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.logout_url,name="logout"),
]