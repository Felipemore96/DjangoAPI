from django.contrib.gis.db import models


# # Create your models here.
# class User(models.Model):
#     age = models.IntegerField()
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
class GeoFeature(models.Model):
    name = models.CharField(max_length=255)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name