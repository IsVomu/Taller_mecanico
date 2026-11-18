from django.contrib import admin
from .models import TipoRepuesto, Repuesto

@admin.register(TipoRepuesto)
class TipoRepuestoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'fecha_ingreso', 'disponible', 'categoria')
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre',)