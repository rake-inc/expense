from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExpenseDetails(models.Model):
    category = models.CharField(max_length=32, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=32, null=False)
    owner = models.ForeignKey(User, to_field='username')
