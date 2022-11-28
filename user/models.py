""" Models for user (one to one relathionship)"""

import logging
import os
import uuid

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Why fight Django's builtin User when you can just do `user.profile`?
    User has: username, first_name, last_name, email, date_joined, is_active, and is_staff
    Profile has the rest!
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user has one rofile")
    upload = models.FileField(upload_to='uploads/profile/')
    gender = models.CharField(max_length=140, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    address = models.TextField(null=True, blank=True) 
