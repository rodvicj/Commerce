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

urlpatterns += router.urls
