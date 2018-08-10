from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    branchcode = models.IntegerField(primary_key=True, unique=True)
    branchname = models.CharField(max_length=45)

    def __str__(self):
        return self.branchname


class Client(models.Model):
    acctid = models.CharField(max_length=30, primary_key=True, unique=True)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    address = models.CharField(max_length=300)
    contactnum = models.CharField(max_length=45)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, related_name='clients')

    def __str__(self):
        return self.lname


