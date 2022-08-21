from django.contrib import admin

from core.models import Exchange, MappingClass, UpdateData, MappingField

admin.site.register(Exchange)
admin.site.register(UpdateData)
admin.site.register(MappingClass)
admin.site.register(MappingField)
