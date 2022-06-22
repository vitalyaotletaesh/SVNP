from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField("Роль", max_length=50)
    title = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"


class User(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(0)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, verbose_name="Роль", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
