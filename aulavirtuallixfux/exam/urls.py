from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.GetFormView.as_view()),
    path('form/<int:pk>',views.GetFormView.as_view()),

    path('question/',views.GetQuestionView.as_view()),
    path('question/<int:pk>',views.GetQuestionView.as_view()),
    
    path('answer/<int:pk>',views.GetAnswerView.as_view()),
    path('answer/',views.GetAnswerView.as_view()),
    path('add_many_answer/',views.complete_answer_form),

    #path('form_complete/',views.complete_form),
    path('get_all_evaluation/<name_course>',views.get_all_evaluation),
    path('get_form_from_course/',views.get_form_course),
]