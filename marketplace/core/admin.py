from django.contrib import admin
from core.models import Category, MeasureUnit, Product

admin.site.register(Product)
admin.site.register(MeasureUnit)
admin.site.register(Category)