from django.contrib.gis.db import models


# Create your models here.
class Shop(models.Model):
    shopName = models.CharField(max_length=100)
    shopLocation = models.PointField()
    shopAddress = models.CharField(max_length=100)
    shopCity = models.CharField(max_length=50)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    userLocation = models.PointField()

    def __str__(self):
        return self.username
