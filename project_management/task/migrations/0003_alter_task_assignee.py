# Generated by Django 4.2.4 on 2023-10-01 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
