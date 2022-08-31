from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Form, Question,Choice,Answer,ShortTextAnswer,LongTextAnswer,SelectOneAnswer



# Este es el serializador de las preguntas:
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        
class ChoiceSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text','is_correct']


# posible problema en el codigo
class QuestionSerializerComplete(serializers.ModelSerializer):
    choices_relations = ChoiceSerializerAdd(many=True,allow_null=True)
    
    def create(self, validated_data):
        question_data = validated_data.pop('choices_relations')
        
        question_model = Question.objects.create(**validated_data)
        for fd in question_data:
            Choice.objects.create(question=question_model,**fd)
            
        return question_model
    
    class Meta:
        model = Question
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices_relations = ChoiceSerializer(many=True,read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

        
class QuestionSerializerAdd(serializers.ModelSerializer):    
    class Meta:
        model = Question
        fields = '__all__'
        

class FormSerializer(serializers.ModelSerializer):
    questions_relations = QuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Form
        fields = ['id','title','description','type_form','evaluation','created','modified','is_active','questions_relations']
        
class FormSerializerAdd(serializers.ModelSerializer):
    questions_relations = QuestionSerializerAdd(many=True)
    
    def create(self, validated_data):
        form_data = validated_data.pop('questions_relations')
        
        form_model = Form.objects.create(**validated_data)
        for fd in form_data:
            Question.objects.create(form=form_model,**fd)
            
        return form_model
    
    class Meta:
        model = Form
        fields = '__all__'
        


class ShortTextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortTextAnswer
        fields = ['answer_text']
    
class LongTextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTextAnswer
        fields = ['answer_text']
    
class SelectOneAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectOneAnswer
        fields = ['answer_text']
        
        
class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    
    answer_short_text = ShortTextAnswerSerializer(read_only=True)
    answer_long_text  = LongTextAnswerSerializer(read_only=True)
    answer_selection_text = SelectOneAnswerSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = '__all__'
        

class AnswerSerializerAdd(serializers.ModelSerializer):
    answer_short_text = ShortTextAnswerSerializer(allow_null=True)
    answer_long_text  = LongTextAnswerSerializer(allow_null=True)
    answer_selection_text = SelectOneAnswerSerializer(allow_null=True)

    def create(self, validated_data):
        shortText_data = validated_data.pop('answer_short_text')
        longText_data = validated_data.pop('answer_long_text')
        selectionText_data = validated_data.pop('answer_selection_text')
        
        answer = Answer.objects.create(**validated_data)
        if shortText_data:
            ShortTextAnswer.objects.create(answer=answer,**shortText_data)
        if longText_data:
            LongTextAnswer.objects.create(answer=answer,**longText_data)
        if selectionText_data:
            SelectOneAnswer.objects.create(answer=answer,**selectionText_data)            
        return answer

    class Meta:
        model = Answer
        fields = '__all__'