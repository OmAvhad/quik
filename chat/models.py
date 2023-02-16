from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import os
from dotenv import load_dotenv

# Create your models here.
class Chats(models.Model):
    
    question = models.TextField(null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    
    class Meta:
        db_table = "chats"
        
class Attachments(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=datetime.now())
    attachment = models.FileField(upload_to='uploads/attachments/',null=True)
    
    class Meta:
        db_table = "attachments"