from django.contrib import admin
from django.contrib.admin.options import StackedInline
from .models import Course,HomeWork,HomeWork,AssignmentSubmission,HistoryClass,Week,ClassWeek,Evaluation,Calification,Certificate,Poll


admin.site.register(Course)
admin.site.register(HomeWork)
admin.site.register(AssignmentSubmission)
admin.site.register(HistoryClass)
admin.site.register(Week)
admin.site.register(ClassWeek)
admin.site.register(Evaluation)
admin.site.register(Calification)
admin.site.register(Certificate)
admin.site.register(Poll)


from .models import DocumentClass,LinkCLass

admin.site.register(DocumentClass)
admin.site.register(LinkCLass)