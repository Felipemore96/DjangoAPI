from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeoFeatureViewSet

router = DefaultRouter()
router.register(r'features', GeoFeatureViewSet, basename='features')

urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),

    # API routes
    path('', include(router.urls)),
]
