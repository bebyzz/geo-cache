__author__ = 'jjh'
from django.db import models
from datetime import datetime
from constants import *


class User(models.Model):
    """
    This is the model for a User instance that represents a row in the User table
    of the database
    """

    user_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=MAX_NAME_LEN)
    surname = models.TextField(max_length=MAX_NAME_LEN)
    email = models.TextField(max_length=MAX_NAME_LEN)


class DDrop(models.Model):
    """
    This is the model for a data drop instance that represents a row in the DDrop table
    of the database
    """

    drop_id = models.AutoField(primary_key=True)
    submitter_id = models.ForeignKey('User', on_delete=models.CASCADE())
    latitude = models.FloatField()
    longitude = models.FloatField()
    data = models.TextField(max_length=MAX_DATA_LEN)
    date_dropped = models.DateField(_("Date"), default=datetime.date.today)