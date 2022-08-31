from django.contrib import admin
from .models import Form,Question,Choice,Answer,ShortTextAnswer,LongTextAnswer,SelectOneAnswer,Choice


class ChoicesInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoicesInline,
    ]
    model = Question

admin.site.register(Question, QuestionAdmin)

# Register your models here.
admin.site.register(Form)
admin.site.register(Choice)

admin.site.register(Answer)


# Campos de los formularios:
admin.site.register(ShortTextAnswer)
admin.site.register(LongTextAnswer)
admin.site.register(SelectOneAnswer)

