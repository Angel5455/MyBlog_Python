from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
#Models
from .models import Post
#admin.site.register(Post)

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen', 'titulo', 'descripcion', 'fecha_creacion')
    list_display_links = ('id', 'titulo')
    list_filter = (('fecha_creacion', DateRangeFilter), ('fecha_act', DateTimeRangeFilter), "titulo")
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('fecha_creacion', 'fecha_act')
