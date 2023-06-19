from rest_framework import serializers
from .models import MessageParams


class MessageParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageParams
        fields = ('bot_token', 'chat_id')