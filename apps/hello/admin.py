from django.contrib import admin

from models import Info




class InfoAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')








admin.site.register(Info, InfoAdmin)



