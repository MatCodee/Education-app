
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    CommentForoView,
    getForoMessageView,
    like_foro
)
from .views import home, send_push

urlpatterns = [
    # Estas son las funcionalidades de los comentarios del foro.
    path("get_foro_course/<slug>",getForoMessageView.as_view()),
    path("add_foro_course/",getForoMessageView.as_view()),
    
    path("get_foro_comment_course/",CommentForoView.as_view()),
    path("get_foro_comment_course/<int:pk>",CommentForoView.as_view()),
    
    
    path("like_acction/",like_foro),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
       
    path('', home),
    path('send_push', send_push),
]