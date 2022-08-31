from asyncore import poll
from django.db.models import query
from django.forms import modelformset_factory
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.db.models import Q

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.contrib.auth.models import User

from users_act.models import Proffesor, Usuario
from users_act.serializers import UserSerializer
# importacion de los modelos
from .models import Course,HomeWork,AssignmentSubmission, Week

# importacion de la serializacion
from .serializers import CourseSerializer,HomeWorkSerializer,CourseSerializeData,CourseSerializeDatas,CourseSerializerImg,AssignmentSubmissionSerializer,CourseSerializerNames,CourseSerializerFull

#---------------------------------------------------------------
# Funciones definidas para los cursoss

# funcion para obtener todos los cursos_
class CourseList(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    

class create_course2(APIView):    
    def post(self, request, format=None):
        if request.method == 'POST':

            course_serializer = CourseSerializeData(data=request.data)
            if course_serializer.is_valid():
                course_serializer.save()
                return Response(course_serializer.data)
            return Response(course_serializer.errors) # mandar el tipo de error





from rest_framework.parsers import MultiPartParser

# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
# crear un nuevo curso solo lo pueden crear los Profesores:
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_course(request):
    if request.method == 'POST':

        course_serializer = CourseSerializeData(data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors) # mandar el tipo de error



# detalle del curso 
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def detail_course(request,slug,*args, **kwargs):
    if request.method == 'GET':
        course = Course.objects.filter(slug=slug).first()
        if course:
            user = {
                'user': request.user
            }
            course_serializer = CourseSerializerFull(course,context=user)
            return Response(course_serializer.data)
        return Response({"course_data": "Error slug no valido"})




from .models import ClassWeek
from .serializers import ClassSerializerWeek

class get_class_from_week(APIView):
    def get(self,request,id):
        class_week = ClassWeek.objects.filter(pk=id).first()
        user = {
            'user': request.user
        }
        serializer = ClassSerializerWeek(class_week,context=user)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




# actualizacion del curso de un professor en este caso:
# TODO: debemos especificar algunos permisos aqui
@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_course_proffesor(request,slug):    
    if request.method == 'PUT':
        course = Course.objects.filter(slug=slug).first()
        course_serializer = CourseSerializeDatas(course,data=request.data,context=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors)


@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_course_proffesor_img(request,slug):
    if request.method == 'PUT':
        course = Course.objects.filter(slug=slug).first()
        course_serializer = CourseSerializerImg(course,data=request.data,context=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors)
# Esta es la funcion para crear clases y a la vez actualizar la clase



########################################################################################

# Eliminar un curso:
# TODO: debemos especificar unos permisos de super usuario para que pueda borrar el curso
@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def delete_course(request,slug):
    if request.method == 'DELETE':
        course = Course.objects.filter(slug=slug).first()
        if course:
            course.delete()
            return Response({"course_data":'Eliminado con extio!'})
        return Response({"course_data": "No se pudo eliminar el curso"})



#-----------------------------------------------------------------
# Funciones definidas para las clases 


# detalle del curso 
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def list_class_course(request,slug):
    if request.method == 'GET':
        course = Course.objects.filter(slug=slug).first()
        course_serializer = CourseSerializeData(course)
        return Response(course_serializer.data)


# Aqui estan las funciones que estan relacionadas con las clases de los cursos
'''
from .models import HistoryClass
from .serializers import HistorySerializer

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_history_courses(request,slug):
    if request.method == 'GET':
        course = Course.objects.filter(slug=slug).first()
        history = HistoryClass.objects.filter(author=request.user,course=course)
        history_serializer = HistorySerializer(history,many=True)
        if history_serializer:
            return  Response(history_serializer)
        else:
            return Response(history_serializer.errors)
'''     



from .serializers import WeekSerializerAdd
# creacion de una semana
class WeekAPIView(APIView):
    def post(self,request):
        serializer = WeekSerializerAdd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            

# Esta es la funcion para devolver las clases------------------------------------------------------------------
from .serializers import ClassSerializerWeekAdd

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getClass(request,id):
    if request.method == 'GET':
        week  = Week.objects.filter(pk=id).first()
        class_course = ClassWeek.objects.filter(week=week)

        if class_course:
            class_serializer = ClassSerializerWeek(class_course,many=True)
            return  Response(class_serializer.data)
        return Response({'data': 'Error no hay clases'})



#@authentication_classes([authentication.TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_class(request):
    if request.method == 'POST':
        data = request.data
        form = {
            'title': data['title'],
            'resumen': data['resumen'],
            'week': data['week'],
            'video': data['video'],
            'url_documents': [],
            'documents': []
        }
        class_serializer = ClassSerializerWeekAdd(data=form)
        print(request.data)
        print(class_serializer.is_valid())
        if class_serializer.is_valid():
            class_serializer.save()
            return Response(class_serializer.data)
        else:
            return Response(class_serializer.errors)


# poder actualizar una clase en particular
@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_class(request,pk):
    if request.method == 'PUT':
        class_data = ClassWeek.objects.filter(id=pk).first()
        class_serializer = ClassSerializerWeekAdd(class_data,data=request.data)
        
        print(request.data)
        print(class_serializer.is_valid())
        if class_serializer.is_valid():
            class_serializer.save()
            return Response(class_serializer.data)
        else: 
            return Response(class_serializer.errors)
        

@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])    
def delete_class(request,pk):
    if request.method == 'DELETE':
        class_data = ClassWeek.objects.filter(id=pk).first()
        if class_data:
            class_data.delete()
            return Response({"class_data":'Eliminado con extio!'})
        return Response({"class_data": "No se pudo eliminar el curso"})

# ------------------------------------------------------------------------------------------------------------------
# Funciones definidas en torno a un usuario


@api_view(['GET'])
def filter_user_course(request,u_name):
    if request.method == 'GET':
        user = Usuario.objects.filter(Q(username=u_name) | Q(email=u_name)).first()
        print(user)
        if user:
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        else:
            return Response({'data': "No encontrado"})
    

@api_view(['POST'])
def add_user_course(request):
    if request.method == 'POST':
        # el slug del curso
        course_request_slug = request.data["course_slug"]
        user_request = request.data["user"]
        
        course = Course.objects.filter(slug=course_request_slug).first()
        # el identificador del usuario
        user = Usuario.objects.filter(username=user_request).first()
        # obtener un curso
        course.usuario.add(user)
        return Response({'data': 'Argegado con extio'})
        
@api_view(['GET'])
def get_user_course(request,slug):
    if request.method == 'GET':
        course = Course.objects.filter(slug=slug).first()
        users = course.usuario.all()

        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data)


# No se si esta funcion va a tener problemas de seguridad en el futuro 

@api_view(['POST']) 
def delete_user_course(request,slug):
    username_data = request.data["username"]
    if request.method == 'POST':

        course_select = Course.objects.filter(slug=slug).first()
        user = course_select.usuario.filter(username=username_data).first()
        course_select.usuario.remove(user)
        return Response({"data":"Exito al ser eliminado"})
    
# -----------------------------------------------------------------------------------------
# Esta es la funcion que va a  agregar un usuario al curso de un autor




# debvolver cursos del usuario usuario que esta authenticado -------------------------------------------------------
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def return_course_user(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        usuario = Usuario.objects.filter(user=user).first() 
        if usuario:
            courses = usuario.course_set.all()
            serializer = CourseSerializer(courses,many=True)
            if serializer:
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({'data': 'error'})







# devolver los cursos creados de cada professor #-----------------------------------------------------------
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def return_course_proffesor(request):
    if request.method == 'GET':
      
        user = User.objects.filter(username=request.user.username).first()
        proffesor = Proffesor.objects.filter(user=user).first() 
        if proffesor:
            courses = Course.objects.filter(author=proffesor)
            serializer = CourseSerializer(courses,many=True)
            if serializer:
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({'data': 'error'})
    
    
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def return_course_proffesor_names(request):
    if request.method == 'GET':
      
        user = User.objects.filter(username=request.user.username).first()
        proffesor = Proffesor.objects.filter(user=user).first() 
        if proffesor:
            courses = Course.objects.filter(author=proffesor)
            serializer = CourseSerializerNames(courses,many=True)
            if serializer:
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({'data': 'error'})



#--------------------------------------------------------------------------
# funciones sin permisos que cualquiera puede acceder a esta funcionalidad

# funcion para hacer una busqueda mas general -----------------------------------------------------------------------------------
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def generalSearch(request):
    query = request.data.get('query','')
    if query:
        course = Course.objects.filter(Q(title__icontains=query) | Q(subtitle__icontains=query))
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
    else:
        return Response({'course_data': []})




# funcion para realizar un filtrado de los cursos -----------------------------------------------------------------------------------
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def generalFilterSearch(request):
    if request.method == "POST":
        params = request.data
        total_course = []
        if not params['nivel']:
            course = Course.objects.filter(Q(category__icontains=params['categoria']) &
                                            Q(tipo_producto__icontains=params['tipo_producto']))
            total_course = course       
        else:
            for i in params['nivel']:
                course = Course.objects.filter(Q(category__icontains=params['categoria']) &
                                                Q(tipo_producto__icontains=params['tipo_producto']) & 
                                                Q(level__icontains=i))
                total_course += course 

        print(total_course)
        serializer = CourseSerializer(total_course,many=True)
        return Response(serializer.data)
    else:
        return Response({'course_data': []})    





# Funciones adicionales detalles de un curso en compra:
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def detail_course_buy(request,slug):
    if request.method == 'GET':
        courses = Course.objects.filter(slug=slug).first()
        courses_serializer = CourseSerializeData(courses)
        if courses_serializer:
            return Response(courses_serializer.data)
        else:
            return Response(courses_serializer.errors)  
        


# TODO: implementasr que recomiende todos  los cursos mejos el  que esta detallado
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def recomend_course_buy(request,category,pk):
    if request.method == 'GET':
        courses = Course.objects.filter(category=category).exclude(id=pk)[:4]
        courses_serializer = CourseSerializeData(courses,many=True)
        if courses_serializer:
            return Response(courses_serializer.data)
        else:
            return Response(courses_serializer.errors)



# --------------------  Vistas de llos envios de tareas  --------------------------------------------------------------
class HomeWorkApiView(APIView):

    # Mostrar todas las clases para un curso determnado
    def get(self,request,id_homework=None):
        #if slug_course:
        #    course = Course.objects.filter(slug=slug_course)
        #    homework = course.homework_set.all()
        #    serializer = HomeWorkSerializer(homework,many=True)
        homework = HomeWork.objects.filter(pk=id_homework).first()
        serializer = HomeWorkSerializer(homework)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    # crear una tarea para cualquier curso
    def post(self,request):
        serializer = HomeWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    # modificar un curso determinado
    def put(self,request,id_homework):
        print(request.data)
        homework = HomeWork.objects.filter(id=id_homework).first()
        serializer = HomeWorkSerializer(homework,data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    # elimnar un curso determinado
    def delete(self,request,id_homework):
        homework = HomeWork.objects.filter(id=id_homework).first()
        if homework:
            homework.delete()
            return Response({ 'data': json.dumps(homework) })
        else:
            return Response({
                'data': json.dumps('Error al eliminar los elementos')
            })
            
    
# para la compatibilidad de la fechas vamos a importar
from dateutil import parser
# envio por parte de los usuarios las tareas
class SendHomeworkAPIView(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    def get(self,request,id_assignment=None):
        homework_detail = AssignmentSubmission.objects.filter(pk=id_assignment).first()    
        serializer = AssignmentSubmissionSerializer(homework_detail)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
    # agregar el campo de id para esto y actualizar el envio del trabajo
    def post(self,request):
        send_homework = AssignmentSubmissionSerializer(data=request.data)
        if send_homework.is_valid():
            send_homework.save()
            return Response(send_homework.data)
        else:
            return Response(send_homework.errors)

    def put(self,request,id_assignment):
        data = request.data
        homework = HomeWork.objects.filter(pk=id_assignment).first()
        assign = AssignmentSubmission.objects.filter(homework=homework,user=data['user']).first()
        print(assign.get_assign())
        print("Mostrando la tarea enviada")
        print(data)
        send_homework = AssignmentSubmissionSerializer(assign,data=data)
        print(send_homework.is_valid())
        if send_homework.is_valid():
            send_homework.save()
            return Response(send_homework.data)
        else:
            return Response(send_homework.errors)


class ListHomeworkStudentAPIView(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    def get(self,request,id_homework):
        homework_detail = HomeWork.objects.filter(pk=id_homework).first()    
        assignmentSubmission = homework_detail.assignmentsubmission_set.all()
        print(assignmentSubmission)
        serializer = AssignmentSubmissionSerializer(assignmentSubmission,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# listas de tareas enfocada a un usuario determinado
class ListHomeworkAPIView(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    def get(self,request):
        homework_not_complete = []
        usuario = Usuario.objects.filter(user=request.user).first() 
        courses = usuario.course_set.all()
        for course in courses:    
            current_homework = HomeWork.objects.filter(course=course,assignmentsubmission__user=usuario,assignmentsubmission__completed=False)
            if current_homework:
                print(current_homework)
                homework_not_complete += current_homework
        
        if homework_not_complete:
            serializer = HomeWorkSerializer(homework_not_complete,many=True)
            return Response(serializer.data)
        else:
            return Response({ 'data': "error"})
        
        
class ListHomeworkAPIViewProfesor(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    
    def get(self,request,course_id):
        course = Course.objects.filter(pk=course_id).first()
        course_home = course.homework_set.all()
        serializer = HomeWorkSerializer(course_home,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ListHomeworkAPIViewProfesorSlug(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]
    
    def get(self,request,course_slug):
        print(course_slug)
        course = Course.objects.filter(slug=course_slug).first()
        course_home = course.homework_set.all()
        print("Mostrando la informacion de los cursos: ")
        print(course_home)
        serializer = HomeWorkSerializer(course_home,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
            
# debvolver cursos del usuario usuario que esta authenticado -------------------------------------------------------
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def return_course_user(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        usuario = Usuario.objects.filter(user=user).first() 
        if usuario:
            courses = usuario.course_set.all()
            serializer = CourseSerializer(courses,many=True)
            if serializer:
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({'data': 'error'})
    


from .models import HistoryClass
from .serializers import HistoryClassSerializer

class HistoryClassAPIView(APIView):
    permission_classes       = [permissions.IsAuthenticated]
    authentication_classes   = [authentication.TokenAuthentication]

    def put(self,request,id):
        data = request.data
        history = HistoryClass.objects.filter(id=id).first()
        serializer = HistoryClassSerializer(history,data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def post(self,request):
        data = request.data
        print(request.data)
        serializer = HistoryClassSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
        
        
from .serializers import EvaluationSerializer

class EvaluationAPIView(APIView):
    def get(self,request,slug):
        courses = Course.objects.filter(slug=slug).first()
        if courses:
            calification_query = courses.evaluation_set.all()        
            serializer = EvaluationSerializer(calification_query,many=True)
            if serializer:
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({'data': 'error'})

    def post(self,request):
        calification = EvaluationSerializer(request.data)
        if calification.is_valid():
            calification.save()
            return Response(calification.data)
        else:
            return Response(calification.errors)
        
        


from .models import Calification
from .serializers import CalificationSerializer


class CalificationAPIView(APIView):
    def get(self,request,slug,username):   
        calification_element = Calification.objects.filter(evaluation__course__slug=slug,usuario__username=username)
        serializer = CalificationSerializer(calification_element,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


from .models import Certificate
from .serializers import CertificateSerializer
class CertificateAPIView(APIView):
    def get(self,request,id_course,id_user):
        certificate = Certificate.objects.filter(course__id=id_course,user__id=id_user).first()
        serializer = CertificateSerializer(certificate)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        
        
from .models import Poll
from .serializers import PollSerializer
class PollAPIView(APIView):
    def get(self,request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
