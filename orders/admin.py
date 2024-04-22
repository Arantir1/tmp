from django.contrib import admin

from .models import Order, Book

admin.site.register(Order)
admin.site.register(Book)
