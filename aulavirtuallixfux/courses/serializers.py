from rest_framework import serializers
from .models import Calification, Course,HomeWork,AssignmentSubmission,HistoryClass,Week,ClassWeek,Poll



# serializador de filter
class filterHistorySerializer(serializers.ListSerializer):
    def to_representation(self, data):
        context = self.context
        if context:
            data = data.filter(user__user__id=context['user'].id)
        return super().to_representation(data)

class HistoryClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryClass
        fields = '__all__'
        list_serializer_class = filterHistorySerializer
    



from .models import DocumentClass,LinkCLass
class DocumentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentClass
        fields = ['title','document']

class LinkClassSerializer(serializers.ModelSerializer):
    class Meta:
        model  = LinkCLass
        fields = ['title','url_document']

class ClassSerializerWeek(serializers.ModelSerializer):    
    histoty_class = HistoryClassSerializer(many=True,read_only=True)
    documents =  DocumentClassSerializer(many=True,allow_null=True)
    url_documents = LinkClassSerializer(many=True,allow_null=True)
        
    class Meta:
        model = ClassWeek
        fields = ['id','title','date_published','resumen','week','video','document','histoty_class','link','documents','url_documents']
        
        
class ClassSerializerWeekAdd(serializers.ModelSerializer):
    documents =  DocumentClassSerializer(many=True,allow_null=True)
    url_documents = LinkClassSerializer(many=True,allow_null=True)

    def create(self, validated_data):
        document_data = validated_data.pop('documents')
        url_document_data = validated_data.pop('url_documents')
        
        class_week_model = ClassWeek.objects.create(**validated_data)
        if(document_data):
            for dd in document_data:
                DocumentClass.objects.create(class_week=class_week_model,**dd)
                
        if(url_document_data):
            for udd in url_document_data:
                LinkCLass.objects.create(class_week=class_week_model,**udd)
                
        return class_week_model
     
    class Meta:
        model = ClassWeek
        fields = ['id','title','date_published','resumen','week','video','document','link','documents','url_documents']



class ClassSerializerNames(serializers.ModelSerializer):    
    histoty_class = HistoryClassSerializer(many=True,read_only=True)
    class Meta:
        model = ClassWeek
        fields = ['id','title','date_published','resumen','histoty_class']

class WeekSerializer(serializers.ModelSerializer):
    week_data = ClassSerializerNames(many=True,read_only=True)
    class Meta:
        model = Week
        fields = ['id','course_week','resumen','week_data','get_profesor','get_fullpath_link']
        
class WeekSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ['course_week','resumen']

class CourseSerializerFull(serializers.ModelSerializer):
    course_data = WeekSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'level',
            'category',
            'tipo_producto',
            'video_hours',
            'student_num',
            'date_published',
            'date_updated',
            'calification',
            'img_course',
            'get_image',
            'get_image_certificate',
            'slug',
            'course_data',
            'end_course',
        ]
        

        
        
        
from .models import Certificate
class CertificateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Certificate
        fields = '__all__'




# Esta es la serializaccion de las tareas
class HomeWorkSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format=None, input_formats=None)
    end_date = serializers.DateField(format=None, input_formats=None)
    class Meta:
        model = HomeWork
        fields = [
            'id',
            'profesor',
            'course',
            'title',
            'description',
            'start_date',
            'end_date',
            # metodos
            'get_proffesorInfo',
            'get_course_info'
        ]
        
class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['id','homework','user','message','document','created_at','completed','get_UserInfo','get_course_info','get_UserImage']






# Esta es la serializacion de los cursos agrupa las ecciones esta en uso ya
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'level',
            'category',
            'tipo_producto',
            'video_hours',
            'student_num',
            'date_published',
            'date_updated',
            'calification',
            'img_course',
            'get_image',
            'get_image_certificate',
            'slug',
            'end_course',
        ]
        
class CourseSerializerNames(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title','slug']



class CourseSerializeData(serializers.ModelSerializer):
    #course_data = ClassSerializerText(many=True,read_only=True)
    class Meta:
        model = Course
        fields = [
            'author',
            'title',
            'subtitle',
            'description',
            'level',
            'category',
            'tipo_producto',
            'date_published',
            'date_updated',
            'img_course',
            #'course_data'
            
            
            # Este es un metodo
            'get_image',
            'end_course',
        ]


class CourseSerializeDatas(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'author',
            'title',
            'subtitle',
            'description',
            'level',
            'category',
            'tipo_producto',
            # Este es un metodo
            'get_image',
            'end_course',
        ]


class CourseSerializerImg(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['author','img_course']
        
        
from .models import Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields= '__all__'
        


class CalificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calification
        fields = ['usuario','nota','porcentaje','get_porcent','get_title_evaluation']
        
class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        
        
        
