from django.db import models

# Create your models here.
class UserType(object):
    REGULAR_USER = "Regular User"
    ADMIN_USER = "Admin User"


class User():

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:

        ordering = ['id']


class UserProfile():

    user = User()
    