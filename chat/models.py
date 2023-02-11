from django.db import models
from datetime import datetime
# Create your models here.
class Chats(models.Model):
    
    question = models.TextField(null=False,blank=False)
    answer = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    
    class Meta:
        db_table = "CHATS"