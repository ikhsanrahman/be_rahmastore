# Generated by Django 3.0.2 on 2020-02-03 09:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200203_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a3074023-4edc-4030-a1f1-a1da3f917be2'), primary_key=True, serialize=False, unique=True),
        ),
    ]
