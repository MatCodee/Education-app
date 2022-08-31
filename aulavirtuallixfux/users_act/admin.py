from django.contrib import admin
from .models import Usuario,Links,Proffesor

class LinksInline(admin.StackedInline):
    model = Links
    extra = 0

class ProffesorAdmin(admin.ModelAdmin):
    inlines = [LinksInline]

admin.site.register(Usuario)
admin.site.register(Proffesor,ProffesorAdmin)
