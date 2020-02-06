# Generated by Django 3.0.2 on 2020-02-02 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200202_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='login_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='logout_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('90c0a43a-fc68-4ba2-a413-8d1be6f87881'), primary_key=True, serialize=False, unique=True),
        ),
    ]
