from rest_framework import serializers
from .models import CommentForo
from users_act.serializers import UserSerializer

from .models import MessageForo

# Funcionalidades especificas de los comentarios

class CommentForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentForo
        fields = '__all__'


class MessageForoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = MessageForo
        fields = '__all__'


class MessageForoSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = MessageForo
        fields = ['user','course','message']