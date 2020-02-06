# Generated by Django 3.0.2 on 2020-02-03 07:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200203_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_uuid',
        ),
        migrations.AddField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9ff2b721-42ec-4a62-8344-e627c8eb60c7'), primary_key=True, serialize=False, unique=True),
        ),
    ]
