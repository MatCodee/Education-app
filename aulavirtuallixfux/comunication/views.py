from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from courses.models import Course
# Create your views here.
from .models import MessageForo
from .serializers import MessageForoSerializer,MessageForoSerializerAdd


# Estas son las funciones principales del foro

class getForoMessageView(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    
    def get(self,request,slug=None):
        course = Course.objects.filter(slug=slug).first()
        foro = MessageForo.objects.filter(course=course) 
        foro_serializer = MessageForoSerializer(foro,many=True)
        if foro_serializer:
            return Response(foro_serializer.data)
        else:
            return Response(foro_serializer.errors)
        
    def post(self,request,slug=None):
        print(request.data)
        foro_serialiezer = MessageForoSerializerAdd(data=request.data)
        print(foro_serialiezer.is_valid())
        if foro_serialiezer.is_valid():
            foro_serialiezer.save()
            return Response(foro_serialiezer.data)
        else:
            return Response(foro_serialiezer.errors)
        
        
    # para estas funciones debes ser el creador del curso
    # funciones de elimina r y actualizar 


# implementacion de las funcionalidades del Foro
from .models import CommentForo
from .serializers import CommentForoSerializer

class CommentForoView(APIView):
    def get(self,request,pk=None):
        if pk:
            comment_foro = CommentForo.objects.filter(id=pk).first()
            serializer = CommentForoSerializer(comment_foro)
        else:
            comment_foro = CommentForo.objects.all()
            serializer = CommentForoSerializer(comment_foro,many=True)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request,pk=None):
        serializer = CommentForoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk=None):
        pass


# operadores de los likes de los mensajes de los nforos y los comentarios
def like_foro(request,id_foro):
    user = request.data
    user_search = MessageForo.objects.get(user__username=user.username)
    message_foro = MessageForo.objects.filter(id=id_foro).first()
    try:
        if user_search:
            # lo eliminamod
            message_foro.delete(user)
            message_foro.save()
        else:
            # lo agregamos
            message_foro.likes.add(user)
            message_foro.save()
        return Response({'data': 'Agregado'})
    except Exception:
        return Response({'data': 'Error'})
    
    
    
# Estas son las notificaciones en el canal de comunicacion:
from django.http.response import HttpResponse
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json

from django.shortcuts import render, get_object_or_404
from django.conf import settings


@require_GET
def home(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   user = request.user
   return render(request, 'home.html', {user: user, 'vapid_key': vapid_key})


@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})