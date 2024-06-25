from django.db import models

# Create your models here.
class data_holding (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.TextField(max_length=500)

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    def __str__(self):
        return self.username