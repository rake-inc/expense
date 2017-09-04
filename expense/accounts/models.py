from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class expense(models.Model):
    category = models.CharField(max_length=32, null=False, blank=True)
    price = models.IntegerField(null=False, blank=True)
    Description = models.TextField(null=False, blank=True)
    owner = models.ForeignKey(User)
