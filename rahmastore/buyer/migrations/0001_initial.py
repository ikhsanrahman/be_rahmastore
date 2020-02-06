# Generated by Django 3.0.2 on 2020-02-02 06:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500, unique=True)),
                ('blacklisted_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['blacklisted_on'],
            },
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_uuid', models.UUIDField(default=uuid.UUID('6f268b0a-1692-4233-91fe-61a9baae705b'), editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('password', models.CharField(max_length=255, unique=True)),
                ('password_hash', models.CharField(max_length=255, unique=True)),
                ('gender', models.CharField(max_length=255)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('house_no', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('postal_code', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('is_login', models.BooleanField(default=True)),
                ('time_login', models.DateTimeField()),
                ('time_logout', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='HistoryBuyer',
            fields=[
                ('history_uuid', models.UUIDField(default=uuid.UUID('54716eac-02af-4271-a3e8-3fbb4e33a442'), editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.Buyer')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_uuid', models.UUIDField(default=uuid.UUID('b380b344-6492-4f70-9770-8cac74249f5e'), editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True)),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='buyer.Buyer')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
