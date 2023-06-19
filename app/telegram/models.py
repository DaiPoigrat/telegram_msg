from django.db import models


# Create your models here.
class MessageParams(models.Model):
    bot_token = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100)
