from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

from werkzeug.security import generate_password_hash, check_password_hash

from buyer.models import BlacklistToken

import uuid
import datetime
import jwt
import os 

key = "3456789adsfdhdfgf%^&IO"

# Create your models here.

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

def uid():
  return uuid.uuid4()


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('have a email address')
        user = self.model(
                    username = username,
                    email = self.normalize_email
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
                    username, email, password=password
            )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):

    id                              = models.UUIDField(primary_key=True, default=uid(), unique=True)
    username                        = models.CharField(
                                        max_length=300, validators = [ RegexValidator(regex = USERNAME_REGEX,
                                            message='Username must be alphanumeric or contain numbers',
                                            code='invalid_username'
                                        )],
                                        unique=True
                                    )
    email                           = models.EmailField( max_length=255, unique=True, verbose_name='email address')
    password_hash                   = models.CharField(max_length=555)
    password                        = models.CharField(max_length=555)
    is_admin                        = models.BooleanField(default=False)
    is_staff                        = models.BooleanField(default=False)
    is_login                        = models.BooleanField(default=False)
    login_at                        = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    logout_at                       = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at                      = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at                      = models.DateTimeField(auto_now_add=True, blank=True)


    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # class Meta:
    #     ordering = ["created_at"]

    def generate_password_hash(self, password) :
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password) :
        return check_password_hash(self.password_hash, password)

    # @staticmethod
    def encode_auth_token(self, user_uuid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_uuid
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        responses= {}
        try:
          payload = jwt.decode(auth_token, os.getenv('JWT_SECRET_KEY', key))
          is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)

          if is_blacklisted_token:
            responses['blacklisted'] = True
            responses['msg'] = 'Token blacklisted. Please log in again.'
            return responses
          else:
            responses['blacklisted'] = False
            responses['msg'] = payload['sub']
            return responses
        except jwt.ExpiredSignatureError:
          return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
          return 'Invalid token. Please log in again.'

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.username

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    