from django.db import models
from users_act.models import Usuario
from courses.models import Evaluation

class Form(models.Model):
    TYPE_FORM = (
        ('Prueba', 'Prueba'),
        ('Encuesta', 'Encuesta'),
        #('Prueba automatizada','Prueba automatizada')
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    type_form = models.CharField(max_length=10, choices=TYPE_FORM, default='Prueba')

    evaluation = models.OneToOneField(Evaluation,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPE_CHOICES = (
        ('short_text', 'Pregunta corta'),
        ('long_text', 'Pregunta larga'),
        ('multiple_text', 'Pregunta multiple'),
    )

    question_text = models.CharField(max_length=200)
    form = models.ForeignKey(Form,related_name='questions_relations',on_delete=models.CASCADE)
    question_type = models.CharField(max_length=15, choices=QUESTION_TYPE_CHOICES, default='short_text')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=300)
    question = models.ForeignKey(Question,related_name='choices_relations',on_delete=models.CASCADE)
    
    # Esto indica si es una respuesta correcta:

    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice_text



# Esta es la respuesta de un usuario
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

class ShortTextAnswer(models.Model):
    answer = models.OneToOneField(Answer,related_name='answer_short_text',on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)

class LongTextAnswer(models.Model):
    answer = models.OneToOneField(Answer,related_name='answer_long_text',on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=5000)
    
    def __str__(self):
        return str(self.id)

class SelectOneAnswer(models.Model):
    answer = models.OneToOneField(Answer,related_name='answer_selection_text',on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=100)

    def __str__(self):
        return self.answer_text

'''
class SelectManyAnswer(Answer):
    choices = models.ManyToManyField(Choice)

    def get_choices(self):
        return ",".join([str(choice) for choice in self.choices.all()])

    def __str__(self):
        return str(self.id)
'''

