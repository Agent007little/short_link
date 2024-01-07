from django.contrib import admin
from .models import ShortLink

# Регистрация модели в админке
admin.site.register(ShortLink)