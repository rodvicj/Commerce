from django.urls import path
from rest_framework import routers

from .views.snippet import SnippetDetail, SnippetList
from .views.user import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register("users", UserViewSet)

urlpatterns = [
    path("snippet", SnippetList.as_view()),
    path("snippet/<int:pk>", SnippetDetail.as_view()),
]

# router.register("snippet", SnippetList.as_view())
# router.register("snippet/<int:pk>", SnippetDetail.as_view())

urlpatterns += router.urls

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
