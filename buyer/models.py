import uuid
from django.db import models

from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash


def uid():
  return uuid.uuid4()

# cart has one to many relation to Product and one to one to buyer
class Cart(models.Model):

    id                          = models.UUIDField(primary_key=True, default=uid(), unique=True)
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

    id = models.UUIDField(primary_key=True, default=uid(), editable=False)
    status = models.CharField(max_length=255, blank=True)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __repr__(self):
        return "<this history is belongs to {}>".format(self.buyer.fullname)

