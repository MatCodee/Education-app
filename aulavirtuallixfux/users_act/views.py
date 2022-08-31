from decimal import Context
from traceback import print_tb
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Proffesor, Usuario
from .serializers import UserSerializer,ProffesorSerializer,ProffesorCompleteSerializer


from .serializers import UserSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

# vistas en las que generamos informaicon del usuario


#------------------------------------------------------------------------------------------------
# Esta representa la informacion del usuario
# TODO: Esta persona debe estar autenticada
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_info(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        user_account = Usuario.objects.filter(user=user).first()
        if user_account:
            user_serializer = UserSerializer(user_account)
            return Response(user_serializer.data)
        else:
            return Response({"errors": "error en obtener informacion de usuario"})
        # else en caso de que falle esto


# Esta retorna la informacion del profesor
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_proffesor_info(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        proffer_account = Proffesor.objects.filter(user=user).first()
        if proffer_account:
            user_serializer = ProffesorCompleteSerializer(proffer_account)
            return Response(user_serializer.data)
        else:
            return Response({"errors": "error en obtener informacion de Proffesor"})
        # else en caso de que falle esto





# Creacion de un usuario a partir del inicio de session
# TODO: NO se guarda el usuario en la base de datos Usuario
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user_data = {
            'username':request.data['username'],
            'email': request.data['email'],
            'fullname': request.data['fullname'],
            'user': request.user.id,
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)





@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_usuario(request):
    if request.method == 'PUT':
        # obtenemos el usuairo que esta authenticado
        user = User.objects.filter(username=request.user.username).first()
        user_account = Usuario.objects.filter(user=user).first()
        print(request.data)
        userSerializer = UserSerializer(user_account,data=request.data,context=request.data)
        print(userSerializer.is_valid())
        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data)
        else:
            return Response(userSerializer.errors)




# Esta es la vista de actualizacion de profesor
@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_proffesor(request):
    if request.method == 'PUT':
        # obtenemos el usuairo que esta authenticado
        user = User.objects.filter(username=request.user.username).first()
        proffesor_account = Proffesor.objects.filter(user=user).first()
        
        proffesorSerializer = ProffesorSerializer(proffesor_account,data=request.data,context=request.data)

        if proffesorSerializer.is_valid():
            proffesorSerializer.save()
            return Response(proffesorSerializer.data)
        else:
            return Response(proffesorSerializer.errors)



# -------------------------------------------------------------------------------------------------
@api_view(['GET'])
def exist_user(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        usuario_account = Usuario.objects.filter(user=user).first()
        if usuario_account:
            return Response({'data':1})
        else:
            return Response({'data':0})
        
@api_view(['GET'])
def getUser(request,id):
    if request.method == 'GET':
        user = User.objects.filter(pk=id).first()
        usuario = Usuario.objects.filter(user=user).first()
        
        usuario = UserSerializer(usuario)
        if usuario:
            return Response(usuario.data)
        else:
            return Response(usuario.errors)    