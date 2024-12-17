from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeoFeatureViewSet

router = DefaultRouter()
router.register(r'features', GeoFeatureViewSet, basename='features')

urlpatterns = [
    path('', include(router.urls)),
]