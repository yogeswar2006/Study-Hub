from django.contrib import admin

# Register your models here.
from .models import Room , message,Topic

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(message)