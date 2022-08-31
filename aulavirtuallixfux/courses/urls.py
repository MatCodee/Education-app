from django.urls import path
from .views import (
    CourseList,
    generalSearch,
    return_course_user,
    list_class_course,
    generalFilterSearch,
    return_course_proffesor,
    create_course2,
    update_course_proffesor,
    return_course_proffesor_names,
    update_course_proffesor_img,
    detail_course,
    getClass,
    update_class,
    delete_class,
    create_class,
    get_user_course,
    add_user_course,
    delete_user_course,
    filter_user_course,
    recomend_course_buy,
    detail_course_buy,

    
    ListHomeworkAPIView,
    HomeWorkApiView,
    SendHomeworkAPIView,
    
    ListHomeworkAPIViewProfesor,
    ListHomeworkAPIViewProfesorSlug,
    ListHomeworkStudentAPIView,
    HistoryClassAPIView,
    get_class_from_week,
    WeekAPIView,
    EvaluationAPIView,
    CalificationAPIView,
    CertificateAPIView,
    PollAPIView,
)

urlpatterns = [
    # clases en las vistas
    path('courses-list/',CourseList.as_view()),
    
    # funciones de cursos de ususarios:
    path('user-course/',return_course_user, name='user_course'),
    
    # funciones de cursos de profesores
    path('proffesor-course/',return_course_proffesor, name='proffesor_course'),
    path('proffesor-course-names/',return_course_proffesor_names,name='proffesor_course_names'),


    #path('create-course/',create_course,name='create_course'),
    path('create-course/',create_course2.as_view(),name='create_course'),

    path('update_proffesor_course/<slug>',update_course_proffesor,name='update_course_proffesor'),
    path('update_proffesor_course_img/<slug>',update_course_proffesor_img,name='update_course_proffesor_img'),
    #path('<slug>/',detail_course,'detail'),
        
    
    path('detail-course/<slug>',detail_course,name='detail-course'),
    path('get_class_from_week/<int:id>',get_class_from_week.as_view()),
    
    
    # funciones de las clases
    path('detail/<slug>', list_class_course,name='detail'),
    path('detail-class/<int:id>',getClass,name='getCLass'),
    path('update_class/<int:pk>',update_class,name=' update_class'),
    path('delete-class/<int:pk>',delete_class,name='delete_class'),
    path('create-class/',create_class,name='create_class'),




    # funciones de Usuario 
    path('add_user_couse/',add_user_course,name='add_user_course'),
    path('get_user_course/<slug>',get_user_course,name='get_user_course'),
    path('delete_user_course/<slug>',delete_user_course,name='delete_user_course'),
    path('filter_user_course/<u_name>',filter_user_course,name='filter_user_course'),


    # funciones en las vistas
    path('search',generalSearch,name='search'),             # LISTO
    path('filter/',generalFilterSearch,name='filter'),      # LISTO
    
    path('recomend_course_buy/<category>/<int:pk>',recomend_course_buy,name='recomend_course_buy'),
    path('detail_course_buy/<slug>',detail_course_buy,name='detail_course_buy'),
    
    
    
    
    # tareas
    path("list_homework/",ListHomeworkAPIView.as_view()),
    path("list_homework_profesor/<course_id>",ListHomeworkAPIViewProfesor.as_view()),
    path("list_homework_profesor_slug/<course_slug>",ListHomeworkAPIViewProfesorSlug.as_view()),
    path("update_list_homework_profesor/<int:id_homework>",HomeWorkApiView.as_view()),
    
    
    
    path('list_homework_student/<int:id_homework>',ListHomeworkStudentAPIView.as_view()),
    
    # operaciones de tareas
    path("add_homework/",HomeWorkApiView.as_view()),
    path("get_homework/<id_homework>",HomeWorkApiView.as_view()),
    
    path("send_homework/",SendHomeworkAPIView.as_view()),
    path("update_Send_homework/<int:id_assignment>",SendHomeworkAPIView.as_view()),
    path("get_send_homework/<int:id_assignment>",SendHomeworkAPIView.as_view()),

    
    # history class
    path("create_history_class/",HistoryClassAPIView.as_view()),
    path("update_history_class/<int:id>",HistoryClassAPIView.as_view()),
    path("get_history_class/<int:course_id>/<int:user_id>",HistoryClassAPIView.as_view()),
    
    
    path('create_week/',WeekAPIView.as_view()),
    
    # funciones de calificaiones del curso
    path('create_calification/',EvaluationAPIView.as_view()),
    path('get_califications/<slug>',EvaluationAPIView.as_view()),
    
    path('get_calification_user/<slug>/<username>',CalificationAPIView.as_view()),
    
    
    
    path('get_certiifcate/<int:id_course>/<int:id_user>',CertificateAPIView.as_view()),
    path('get_polls/',PollAPIView.as_view()),
]
