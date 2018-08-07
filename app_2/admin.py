from django.contrib import admin

from haystack.admin import SearchModelAdmin
#from djangocms_internalsearch.search_all_admin import SearchModelAdmin

from .models import (
    Model1,
    Model2,
)


# Register your models here.

class Model1Admin(admin.ModelAdmin):
    search_fields = ('fchar',)
    list_filter = ('fdate', 'fdatetime', 'fbool', 'fint', 'fdeci')
    list_display = ('fdate', 'fdatetime', 'fbool', 'fint', 'fdeci')


class Model2Admin(admin.ModelAdmin):
    search_fields = ('f2char',)
    list_filter = ('f2date', 'f2datetime', 'f2bool', 'f2int', 'f2deci')

class Model2SAdmin(SearchModelAdmin):
    search_fields = ('f2char',)
    #list_filter = ('f2date', 'f2datetime', 'f2bool', 'f2int', 'f2deci')


admin.site.register(Model1, Model1Admin)
#admin.site.register(Model2, Model2Admin)
admin.site.register(Model2, Model2SAdmin)

