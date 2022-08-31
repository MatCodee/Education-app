from distutils.command.upload import upload
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from cProfile import Profile
from importlib.metadata import files
from django.db import models
from django.contrib.auth.models import User
from users_act.models import Proffesor, Usuario

# Este es el path de direccionamiento de localhost
from main.settings import PATH_PAGE
import os
from django.conf import settings
from django.utils import timezone
from pathlib import Path

# direccion de directorio de course


def upload_location_course(instance, filename):
    file_path = '{owner_id}/{name_course}/course_img.jpg'.format(
        owner_id=str(instance.author.id), name_course=str(instance.title))
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path


class Course(models.Model):
    LEVELS_COURSE = [
        ('Todos los niveles', 'Todos los niveles'),
        ('Basico', 'Basico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    CATEGORY = [
        ('Tegnologia', 'Tegnologia'),
        ('Administracion', 'Administracion'),
        ('Negocios', 'Negocios'),
        ('Contabilidad', 'Contabilidad'),
        ('Comunicacion', 'Comunicacion'),
        ('Salud', 'Salud'),
        ('Educacion', 'Educacion'),
    ]

    TIPO_PRODUCTO = [
        ("Curso", "Curso"),
        ("Programa Especializado", "Programa Especializado"),
    ]

    author = models.ForeignKey(Proffesor, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    level = models.CharField(max_length=20, choices=LEVELS_COURSE, default=1)
    category = models.CharField(max_length=20, choices=CATEGORY, default=1)
    tipo_producto = models.CharField(
        max_length=30, choices=TIPO_PRODUCTO, default=1)

    video_hours = models.FloatField(default=0)
    student_num = models.IntegerField(default=0)

    calification = models.FloatField(default=0, blank=True, null=True)

    # no se porque no funciona esto
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")

    img_course = models.ImageField(
        upload_to=upload_location_course, blank=True)
    img_certificate = models.ImageField(
        upload_to=upload_location_course, null=True, blank=True)

    end_course = models.BooleanField(default=0)
    usuario = models.ManyToManyField(Usuario, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    # Esta es la funcion que va a aeliminar las imagenes de los cursos

    def delete_course_image(self):
        pass

    def get_image(self):
        if self.img_course:
            return self.img_course.url
        return ''

    def get_image_certificate(self):
        if self.img_certificate:
            return PATH_PAGE + self.img_certificate.url
        return ''

    def __str__(self):
        return f"titulo: {self.title} - Profesor: {self.author.user.username}"


def upload_certificate(instance, filename):
    file_path = '{owner_id}/{name_course}/certificate/certificado.pdf'.format(
        owner_id=str(instance.course.author.id), name_course=str(instance.course.title))
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path


class Certificate(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certificate = models.FileField(
        upload_to=upload_certificate, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} / {self.course.title}"


def upload_foro_messages(instance, filename):
    extension = 'file' + Path(filename).suffix
    file_path = 'foro/store/' + extension

    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path



# Modelos genericos de almacenamiento de Datos

def file_upload_path(instance):
    file_path = '{owner_id}/{name_course}/calification/{filename}'.format(
        owner_id=str(instance.course.author.id),
        name_course=str(instance.course.title),
        filename=filename
    )
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path

class File(models.Model):
    file = models.FileField(upload_to=file_upload_path)

    def __str__(self):
        return self.foro.message


# Esta es la configuracion de la semana:
class Week(models.Model):
    course_week = models.ForeignKey(
        Course, related_name='course_data', on_delete=models.CASCADE)
    resumen = models.TextField(blank=True)

    def get_fullpath_link(self):
        file_path = '{name_course}/semana-{semana}'.format(
            name_course=str(self.course_week.id), semana=str(self.id))
        return file_path

    def get_profesor(self):
        return self.course_week.author.user.username


def upload_location_file_calification(instance, filename):
    file_path = '{owner_id}/{name_course}/calification/{filename}'.format(
        owner_id=str(instance.course.author.id),
        name_course=str(instance.course.title),
        filename=filename
    )
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path


def upload_location_file_week(instance, filename):
    extension = 'file' + Path(instance.title).suffix
    file_path = "{owner_id}/{name_course}/clase/{extension}".format(
        owner_id=str(instance.class_week.week.course_week.author.id), name_course=str(instance.class_week.week.course_week.title), extension=str(extension))
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path


class ClassWeek(models.Model):
    title = models.CharField(max_length=500)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    resumen = models.TextField(blank=True)
    week = models.ForeignKey(
        Week, related_name='week_data', on_delete=models.CASCADE)

    # agregar mas elementos
    video = models.URLField(null=True, blank=True)
    document = models.FileField(
        upload_to=upload_location_file_week, blank=True)
    link = models.URLField(null=True, blank=True)

    # Esta es la funcion que va a eliminar los archivos aws de video y documento

    def __str__(self):
        return self.title


class LinkCLass(models.Model):
    class_week = models.ForeignKey(
        ClassWeek, related_name='url_documents', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    url_document = models.URLField()

    def __str__(self):
        return self.title


class DocumentClass(models.Model):
    class_week = models.ForeignKey(
        ClassWeek, related_name='documents', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    document = models.FileField(
        upload_to=upload_location_file_week, blank=True)

    def __str__(self):
        return self.title


class HistoryClass(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    class_course = models.ForeignKey(
        ClassWeek, related_name='histoty_class', on_delete=models.CASCADE)
    completed_class = models.BooleanField(default=False)


def upload_location_homework_file(instance, filename):
    extension = 'file' + Path(filename).suffix
    file_path = '{owner_id}/{name_course}/clases/homework/{filename}'.format(
        owner_id=str(instance.clase.course.author.id),
        name_course=str(instance.clase.course.title),
        clase=str(instance.clase.title),
        filename=extension
    )
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path


# Tareas de las personas debe estar conectada  para que los profesoras puedan ver
# presentacion del homework del estudiante
class HomeWork(models.Model):
    profesor = models.ForeignKey(Proffesor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_file = models.ManyToManyField('FileContent', blank=True)
    link_content = models.ManyToManyField('LinkPage', blank=True)
    start_date = models.DateTimeField(verbose_name="date start")
    end_date = models.DateTimeField(verbose_name="date end")

    def get_proffesorInfo(self):
        return self.profesor.user.username

    def get_course_info(self):
        return self.course.title


def upload_location_evaluation_file(instance, filename):
    extension = 'file' + Path(filename).suffix
    file_path = '{owner_id}/{name_course}/clases/evaluation/{filename}'.format(
        owner_id=str(instance.clase.course.author.id),
        name_course=str(instance.clase.course.title),
        clase=str(instance.clase.title),
        filename=extension
    )
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path

# Estas son las encuestas


class Poll(models.Model):
    profesor = models.ForeignKey(Proffesor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    document = models.FileField(
        upload_to=upload_location_evaluation_file, null=True, blank=True)
    start_date = models.DateTimeField(verbose_name="date start")
    end_date = models.DateTimeField(verbose_name="date end")


class Evaluation(models.Model):
    profesor = models.ForeignKey(Proffesor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    document = models.FileField(
        upload_to=upload_location_evaluation_file, null=True, blank=True)
    start_date = models.DateTimeField(verbose_name="date start")
    end_date = models.DateTimeField(verbose_name="date end")
    porcentaje = models.IntegerField(default=25)


class Calification(models.Model):
    evaluation = models.ForeignKey(
        Evaluation, related_name='data_calification', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.FloatField()
    date_created = models.DateField(auto_now_add=True)
    porcentaje = models.IntegerField(default=25)

    def get_porcent(self):
        return self.evaluation.porcentaje

    def get_title_evaluation(self):
        return self.evaluation.title

    def __str__(self):
        return f"{self.usuario.username}-Titulo evaluacion: {self.evaluation.title}"


def upload_location_assigment_file(instance, filename):
    extension = 'file' + Path(filename).suffix
    file_path = '{owner_id}/{name_course}/clases/assignment/{filename}'.format(
        owner_id=str(instance.clase.course.author.id),
        name_course=str(instance.clase.course.title),
        clase=str(instance.clase.title),
        filename=extension
    )
    fullpath = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(fullpath):
        os.remove(fullpath)
    return file_path


# envio de tarea del estudiante
class AssignmentSubmission(models.Model):
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    document = models.FileField(
        upload_to=upload_location_assigment_file, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="date end")
    completed = models.BooleanField(default=False)

    def get_UserInfo(self):
        return self.user.username

    def get_UserImage(self):
        return self.user.get_image

    def get_course_info(self):
        return self.homework.title

    def get_assign(self):
        elemt = {
            'homework': self.homework,
            'user': self.user,
            'message': self.message,
            'document': self.document,
            'completed': self.completed,
        }
        return elemt


@receiver(post_save, sender=HomeWork)
def create_AssignmentSubmission(sender, instance, created, **kwargs):
    if created:
        course = Course.objects.filter(homework=instance).first()
        users = course.usuario.all()
        for user in users:
            if not AssignmentSubmission.objects.filter(homework=instance, user=user).exists():
                AssignmentSubmission.objects.create(
                    homework=instance, user=user).save()


class LinkPage(models.Model):
    date_created = models.DateField(auto_now_add=True)
    link = models.URLField()


class FileContent(models.Model):
    date_created = models.DateField(auto_now_add=True)
    description_file = models.FileField(
        upload_to=upload_location_homework_file, blank=True, null=True)


'''
class HistoryClass(models.Model):
    author = models.OneToOneField(Usuario,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    finish = models.BooleanField(default=False)
    class_data = models.OneToOneField(ClassCourse,on_delete=models.CASCADE)
'''
# ---------------------------------------------------------------------------------------
# TODO: falta implementar un metodo para borrar los documentos desde la nube
# ---------------------------------------------------------------------------------------


# la persona que esta conectada en la session defuinida

# esta es la funcion que va a generar el slug por defecto
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f"slug-{instance.title}")


pre_save.connect(pre_save_blog_post_receiver, sender=Course)
