from django.contrib.gis.db import models
from django.core.exceptions import ValidationError

# Class to obtain feature objects from GeoJSON file    
class GeoFeature(models.Model):
    name = models.CharField(max_length=255)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name

# Model validation to ensure only valid geometries are stored
def clean(self):
    if not self.geom:
        raise ValidationError("Geometry field cannot be empty")

# Test class
# class User(models.Model):
#     age = models.IntegerField()
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name