from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.filters import InBBoxFilter  # For bounding box filtering
from .models import GeoFeature
from .serializer import GeoFeatureSerializer

# @api_view(['GET'])
# def get_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeoFeatureViewSet(ModelViewSet):
    queryset = GeoFeature.objects.all()
    serializer_class = GeoFeatureSerializer
    # permission_classes = [IsAuthenticated] Something similar to this can be added to authenticate users

    # Bounding box filter setup
    bbox_filter_field = "geom"  # Specifies the geometry field to filter on
    filter_backends = [InBBoxFilter]
    bbox_filter_include_overlapping = True  # Include features overlapping the bounding box

