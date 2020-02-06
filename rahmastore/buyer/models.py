import uuid

from django.db import models

from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash

from product.models import Product

from config.config import Config

TIME = Config().time()

def uid():
  return uuid.uuid4()


class Buyer(models.Model):

    id                          = models.UUIDField(primary_key=True, default=uid(), editable=False)
    fullname                    = models.CharField(max_length=255)
    email                       = models.EmailField(max_length=255, unique=True, blank=True)
    password                    = models.CharField(max_length=255, unique=True)
    password_hash               = models.CharField(max_length=255, unique=True)
    gender                      = models.CharField(max_length=255)
    address_line1               = models.TextField()
    address_line2               = models.TextField()
    house_no                    = models.CharField(max_length=100)
    phone_number                = models.IntegerField()
    postal_code                 = models.CharField(max_length=100)
    city                        = models.CharField(max_length=100)
    province                    = models.CharField(max_length=100)
    country                     = models.CharField(max_length=100)
    is_login                    = models.BooleanField(default=True)
    time_login                  = models.DateTimeField(auto_now_add=False)
    time_logout                 = models.DateTimeField(auto_now_add=False)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']

    def generate_password_hash(self, password) :
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password) :
        return check_password_hash(self.password_hash, password)

    # @staticmethod
    def encode_auth_token(self, buyer_uuid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': buyer_uuid
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
        try:
          payload = jwt.decode(auth_token, os.getenv('JWT_SECRET_KEY'))
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

    def __repr__(self):
        return self.fullname


# cart has one to many relation to Product and one to one to buyer
class Cart(models.Model):

    id                          = models.UUIDField(primary_key=True, default=uid(), unique=True)
    buyer                       = models.OneToOneField(Buyer, on_delete=models.CASCADE)
    is_active                   = models.BooleanField(default=True)
    created_at                  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deleted_at                  = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        pass

    def __repr__(self):
        return "<this cart belongs to {}>".format(self.buyer.fullname)

#history has one to many relation to product that has been bought
class HistoryBuyer(models.Model):

    id                          = models.UUIDField(primary_key=True, default=uid(), editable=False)
    buyer                       = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    status                      = models.CharField(max_length=255, blank=True)
    amount                      = models.IntegerField()
    created_at                  = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __repr__(self):
        return "<this history is belongs to {}>".format(self.buyer.fullname)


class BlacklistToken(models.Model):
  """
  Token Model for storing JWT tokens
  """

  token                         = models.CharField(max_length=500, unique=True)
  blacklisted_on                = models.DateTimeField(auto_now_add=True)

  class Meta:
        ordering = ['blacklisted_on']

  @staticmethod
  def check_blacklist(auth_token):
    res = BlacklistToken.objects.filter(token=auth_token)

    if res:
        return True
    else:
        return False

  def __repr__(self):
    return '<id: token: {}'.format(self.token)