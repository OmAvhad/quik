from django.urls import path
from . import views,api

app_name = "chat"

urlpatterns = [
    #templates
    path('',views.chat,name="home"),
    path('dashboard',views.dashboard,name="dashboard"),
    
    #APIs
    path('v1/get-response',api.getResponse,name="get-response")
]