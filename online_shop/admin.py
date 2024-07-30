from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
