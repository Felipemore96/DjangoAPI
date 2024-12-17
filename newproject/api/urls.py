# from .views import get_users, create_user
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeoFeatureViewSet

# urlpatterns = [
#     # path('users/', get_users, name='get_user'),
#     # path('users/create/', create_user, name='create_user')
#     path('api/features/', GeoFeatureViewSet, name='Features')
# ]

# # Create a router and register the GeoFeatureViewSet
# router = DefaultRouter()
# router.register(r'features', GeoFeatureViewSet, basename='features')

# # Include the router URLs
# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

router = DefaultRouter()
router.register(r'features', GeoFeatureViewSet, basename='features')

urlpatterns = [
    path('', include(router.urls)),  # This automatically handles /api/features/
]