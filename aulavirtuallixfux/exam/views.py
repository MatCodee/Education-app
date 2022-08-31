from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from courses.models import Evaluation


from .models import Form, Question,Answer
from .serializers import FormSerializer,QuestionSerializer,AnswerSerializer,AnswerSerializerAdd,QuestionSerializerAdd,FormSerializerAdd,QuestionSerializerComplete
# Devuelve todos los formularios creados por el usuario:

class GetFormView(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    
    # Traer todos os formulaarios o uno solo
    def get(self,request,pk=None):
        if pk:
            # le pasamos el id de la evaluacion
            form = Form.objects.filter(evaluation=pk).first()
            print("Mostrando el formulario: ")
            print(form)
            serializer = FormSerializer(form)
        else:
            form = Form.objects.all()
            serializer = FormSerializer(form,many=True)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # Crear un formulario
    def post(self,request,pk=None):
        serializer = FormSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # Actualizar un formulario
    def put(self,request,pk=None):
        # El id que se le pasa es un id de formulario
        form = Form.objects.filter(id=pk).first()
        serializer = FormSerializer(form,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # eliminar un formulario
    def delete(self,request,pk=None):
        form = Form.objects.filter(id=pk).first()
        if form:
            form.delete()
            return Response({"course_data":'Eliminado con extio!'},status=status.HTTP_200_OK)
        return Response({"course_data": "No se pudo eliminar el curso"},status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class GetQuestionView(APIView):
    #permission_classes       = [permissions.IsAuthenticated]
    #authentication_classes   = [authentication.TokenAuthentication]
    
    # Traer todos os formulaarios o uno solo
    def get(self,request,pk=None):
        if pk:
            question = Question.objects.filter(id=pk).first()
            serializer = QuestionSerializer(question)
        else:
            question = Question.objects.all()
            serializer = QuestionSerializer(question,many=True)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request,pk=None):
        data = request.data
        print(data)
        if len(data) > 1:
            for element in data:
                serializer = QuestionSerializerComplete(data=element)
                print(serializer.is_valid())
                print(serializer.errors)
                if serializer.is_valid():
                    serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # Actualizar un formulario
    def put(self,request,pk=None):
        question = Question.objects.filter(id=pk).first()
        serializer = QuestionSerializer(question,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # eliminar un formulario
    def delete(self,request,pk=None):
        question = Question.objects.filter(id=pk).first()
        if question:
            question.delete()
            return Response({"course_data":'Eliminado con extio!'},status=status.HTTP_200_OK)
        return Response({"course_data": "No se pudo eliminar el curso"},status=status.HTTP_400_BAD_REQUEST)
    

class GetAnswerView(APIView):
    #permission_classes       = [permissions.IsAuthenticated]
    #authentication_classes   = [authentication.TokenAuthentication]
    
    def get(self,request,pk=None):
        if pk:
            answer = Answer.objects.filter(id=pk).first()
            serializer = AnswerSerializer(answer)
        else:
            answer = Answer.objects.all()
            serializer = AnswerSerializer(answer,many=True)
        if serializer:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
    def post(self,request,pk=None):       
        serializer = AnswerSerializerAdd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
'''
@api_view(['POST'])
def complete_form(request):
    form = request.data['form']
    questions = request.data['questions']
    
    form_serializer = FormSerializer(data=form)
    if form_serializer.is_valid():
        form_serializer.save()
        
        for question in questions:
            question_serializer = QuestionSerializerComplete(data=question)
            if question_serializer.is_valid():
                question_serializer.save()
        return Response(form_serializer.data)
    return Response(form_serializer.errors)
''' 

from courses.serializers import EvaluationSerializer

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_all_evaluation(request,name_course):
    evaluation = Evaluation.objects.filter(course__title=name_course)
    serializer = EvaluationSerializer(evaluation,many=True)
    if serializer:
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(Response.errors,status=status.HTTP_400_BAD_REQUEST)
    
# Este trae
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_form_course(request,name_course):
    evaluation = Evaluation.objects.filter(course__title=name_course)
    form = Form.objects.filter(evaluation=evaluation).first()
    serializer = FormSerializer(form)
    if serializer:
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(Response.errors,status=status.HTTP_400_BAD_REQUEST)



# Esta es la funcion que va a crear un formulario con las respuesta de los usuarios
@api_view(['POST'])
def complete_answer_form(request):
    data = request.data
    print(data)
    if len(data) > 1:
        for d in data:
            serializer = AnswerSerializerAdd(data=d)
            print(serializer.is_valid())
            print(serializer.errors)
            if serializer.is_valid():
                serializer.save()
        # Devuelve el ultimo agregado de respuestas
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
