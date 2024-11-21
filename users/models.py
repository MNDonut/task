from django.db import models


# don't inherit from AbstractUser because by the requirement there should be only 2 fields
class User(models.Model):
    username = models.CharField(max_length=63, unique=True)
    email = models.EmailField()
