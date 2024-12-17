# from rest_framework import serializers
# from .models import User
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import GeoFeature


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class GeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GeoFeature
        geo_field = "geom"
        fields = "__all__"