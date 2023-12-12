from rest_framework.routers import SimpleRouter

from commerce_core.auctions.views.address import AddressViewSet
from commerce_core.auctions.views.product import ProductViewSet

router = SimpleRouter(trailing_slash=False)
router.register("products", ProductViewSet)
router.register("address", AddressViewSet)

urlpatterns = router.urls
