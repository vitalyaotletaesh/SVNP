from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Role(models.Model):
    name = models.CharField("Роль", max_length=50)
    title = models.TextField("Описание", default='')

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, verbose_name="Роль", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Project(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор")
    name = models.CharField(max_length=200, verbose_name="Имя")
    title = models.TextField("Описание", default='')
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class File(models.Model):
    file_version = models.CharField(max_length=3, verbose_name="Версия файла")
    file_change_date = models.DateTimeField(default=timezone.now)
    file_upload = models.FileField(upload_to='project_data/SVNP/', null=True, blank=True, verbose_name="Загрузите файл")


