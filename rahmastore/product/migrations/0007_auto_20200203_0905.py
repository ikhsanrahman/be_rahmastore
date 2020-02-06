# Generated by Django 3.0.2 on 2020-02-03 09:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200203_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, default='fzqjla9c6i', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('220c86ab-87ab-4157-b46c-6140a04af26d'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0c7e2f64-c5b2-4d1b-a0b9-575448747b77'), primary_key=True, serialize=False, unique=True),
        ),
    ]
