# Generated by Django 3.2.13 on 2022-06-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SVNP', '0002_role_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
