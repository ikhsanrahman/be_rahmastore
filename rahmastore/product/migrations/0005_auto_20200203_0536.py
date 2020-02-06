# Generated by Django 3.0.2 on 2020-02-03 05:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200202_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, default='m3kvaapxh1', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_uuid',
            field=models.UUIDField(default=uuid.UUID('064eda5f-4c2f-4724-94a0-54dc9b28867d'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='picture_uuid',
            field=models.UUIDField(default=uuid.UUID('92b71c54-0aa5-49f5-a9d5-9cafe6679c58'), primary_key=True, serialize=False, unique=True),
        ),
    ]
