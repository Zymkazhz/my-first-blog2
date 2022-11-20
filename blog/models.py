from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):  # определяем нашу модель (обьект)
    # models.Model - означет, что обект Post является моделью Джанго , так Джанго поймет, что он должен сохранить его в базу данных
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Автор. Ссылка на другую модель
    title = models.CharField(max_length=200)  # Заголовок. models.CharFieald определяет текстовое поле с ограниченными кол-во символами
    text = models.TextField()  # Текст. models.TextField определяет с неограничинным кол-во текста
    created_date = models.DateTimeField(default=timezone.now)  # Дата создания. models.DateTimeField определяет дату и время
    published_date = models.DateTimeField(blank=True, null=True)  # Дата опубликования. models.DateTimeField определяет дату и время

    def publish(self):  # Метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #    Метод возвращающий текст с заголовком записи
        return self.title