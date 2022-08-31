from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.contrib.auth import get_user_model

import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime,timezone

# Creo que es mejor que cada usurio pueda registrase y tenga la misma posibilidad de poder
# ser un profesor dentro de la plataforma 
    
def upload_location_user(instance, filename):
    file_path = '{owner_id}/{username}/default.jpg'.format(
				owner_id=str(instance.user.id),username=str(instance.username))
    fullpath = os.path.join(settings.MEDIA_ROOT,file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path

class Usuario(models.Model):
    username = models.CharField(max_length=50,unique=True)
    fullname = models.CharField(blank=True,max_length=150)
    email = models.EmailField(blank=True)
    
    is_instructor = models.BooleanField(default=False)

    # usuarios de igual forma tienen imagen
    last_connect = models.DateTimeField(default=datetime.now())

    # necesita un usuario par apoder crear este usuario
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    image_user = models.ImageField(default="users/default_user.png",upload_to=upload_location_user,null=True,blank=True)


    # Esta funcion debemos hacer una modificacion a la dimension
    @property
    def get_image(self):
        if self.image_user:
            return self.image_user.url
        return ''

    def __str__(self):
        return self.username



class Proffesor(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)

    description         = models.TextField(blank=True,null=True)
    resumen             = models.TextField(blank=True,null=True) 

    def __str__(self):
        return self.user.username
        

class Links(models.Model):
    links = [
        (1,'Gmail'),
        (2,'Facebook'),
        (3,'Instagram'),
        (4,'Whatsapp'),
        (5,'Github'),
    ]

    name_link           = models.IntegerField(choices=links,default=1)
    link                = models.URLField()
    proffesor           = models.ForeignKey(Proffesor,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.links[int(self.name_link)-1])



@receiver(post_save,sender=User)    
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Usuario.objects.create(user=instance,username=instance.username,email=instance.email)
        Proffesor.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.user.save()
    instance.proffesor.save()


