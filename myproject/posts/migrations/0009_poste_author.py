# Generated by Django 4.2.11 on 2024-04-30 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_poste_evenement_logement_recommandation_stage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]