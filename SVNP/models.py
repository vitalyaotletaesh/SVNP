from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.TextField("Описание", default='')

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Role(models.Model):
    name = models.CharField("Роль", max_length=50)
    title = models.TextField("Описание", default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class User(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=0)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, verbose_name="Роль", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
