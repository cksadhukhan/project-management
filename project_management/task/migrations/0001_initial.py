# Generated by Django 4.2.4 on 2023-10-01 19:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('inprogress', 'In Progress'), ('inreview', 'In Review'), ('done', 'Done')], default='todo', max_length=20)),
            ],
            options={
                'db_table': 'tasks',
                'ordering': ['-created_at'],
            },
        ),
    ]
