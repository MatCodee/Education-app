from django.db import models
from users_act.models import Proffesor, Usuario
from courses.models import Course
from django.utils import timezone
from django.conf import settings
from pathlib import Path
import os



def upload_foro_messages(instance, filename):
    extension = 'file' + Path(filename).suffix
    file_path = 'foro/store/' + extension

    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path



class MessageForo(models.Model):
    # debe ser many to many ya que van a participar varioas personas en el foro
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # error debe ser OnetoFieds
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateField(default=timezone.now)
    
    likes = models.ManyToManyField(Usuario, blank=True, related_name='usuarios')
    comment_nums = models.IntegerField(default=0)
    

    images = models.ImageField(
        upload_to=upload_foro_messages, blank=True, null=True)
    documents = models.FileField(
        upload_to=upload_foro_messages, blank=True, null=True)
    link = models.URLField(blank=True, null=True)



class CommentForo(models.Model):
    foro = models.ForeignKey(MessageForo, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    date_created = models.DateField(default=timezone.now)

    images_comment = models.ImageField(
        upload_to=upload_foro_messages, blank=True, null=True)
    documents_comment = models.FileField(
        upload_to=upload_foro_messages, blank=True, null=True)
    link_comment = models.URLField(blank=True, null=True)