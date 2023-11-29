from rest_framework.routers import SimpleRouter

from .views.product import ProductViewSet

router = SimpleRouter(trailing_slash=False)
router.register("products", ProductViewSet)

urlpatterns = router.urls
