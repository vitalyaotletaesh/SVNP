# Generated by Django 3.2.13 on 2022-06-22 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SVNP', '0004_auto_20220621_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]