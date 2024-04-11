from django.db import models
from django.contrib.auth.models import AbstractUser

from shop.settings import AUTH_USER_MODEL
from store.models import Product

# Create your models here.
class Shopper(AbstractUser):
    pass

