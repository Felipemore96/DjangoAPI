from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import GeoFeature

class GeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GeoFeature
        geo_field = "geom"
        fields = ('id', 'name', 'geom')

    def validate_geom(self, value):
        # Additional validation can be added here if necessary
        return value