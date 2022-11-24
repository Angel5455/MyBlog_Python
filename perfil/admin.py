from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
#Models
from .models import Project
#admin.site.register(Project)


@admin.register(Project)
class postAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'fecha_creacion')
    list_editable= ('titulo',)
    list_filter = ('fecha_creacion', 'fecha_act')
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('fecha_creacion', 'fecha_act')
