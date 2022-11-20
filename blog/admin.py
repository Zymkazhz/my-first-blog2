from django.contrib import admin
from .models import Post

admin.site.register(Post)  # Что бы наша модель была доступна на странице администратирования, мы её зарегистрирвоали
