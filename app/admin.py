from django.contrib import admin
from .models import *

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('codigo_equipo', 'nombre', 'descripcion')
	search_fields = ['nombre']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apodo', 'fecha_nacimiento', 'edad', 'rut')
	search_fields = ['nombre', 'apodo', 'rut']
	list_filter = ['team']
# Register your models here.
