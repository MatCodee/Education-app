from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Proffesor, Usuario



class UserSerializer(serializers.ModelSerializer):
    #user = UserModelSerializer(read_only=True)
    
    class Meta:
        model = Usuario
        fields = "__all__"


class ProffesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffesor
        fields = ['user','description','resumen']


class ProffesorCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffesor
        fields = "__all__"