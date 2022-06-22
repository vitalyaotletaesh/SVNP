# Generated by Django 3.2.13 on 2022-06-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SVNP', '0005_auto_20220622_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Роль', 'verbose_name_plural': 'Роли'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]