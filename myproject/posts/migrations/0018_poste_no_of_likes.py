# Generated by Django 4.2.11 on 2024-05-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
