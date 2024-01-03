# from django.urls import include, path
from rest_framework import routers

from .views.user import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# urlpatterns += router.urls

# from rest_framework.routers import SimpleRouter

# from .views.user import UserViewSet

# router = SimpleRouter(trailing_slash=False)
# router.register('users', UserViewSet)

# urlpatterns = router.urls
