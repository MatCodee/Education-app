from django.urls import path
from . import views

urlpatterns = [
    path("infoUser/",views.get_user_info,name='getUser'),
    path("infoProffesor/",views.get_proffesor_info,name='get_proffesor_info'),
    path("createUser/",views.create_user,name='create_user'),
    path("exist_user/",views.exist_user,name='exist_user'),

    path('update_usuario/',views.update_usuario,name='update_usuario'),
    path('update_proffesor/',views.update_proffesor,name='update_proffesor'),
    
    path('get_user/<int:id>',views.getUser,name='getUser'),
]

