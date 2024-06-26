from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Product
from ..models.product import ActivationStatus
from ..serializers.product import ProductReadSerializer, ProductWriteSerializer

User = get_user_model()


class ProductViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        read_serializer = ProductReadSerializer(product, context={"request": request})

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user

        if self.action in ["create", "partial_update", "update"]:
            return Product.objects.filter(seller=user)
        else:
            return Product.objects.filter(
                Q(activation_status=ActivationStatus.ACTIVE) |
                Q(activation_status=ActivationStatus.DRAFT, seller=user)
            )

    def get_serializer_class(self):
        if self.action in ["create", "partial_update", "update"]:
            return ProductWriteSerializer

        return ProductReadSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={"request": request}, partial=partial)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        read_serializer = ProductReadSerializer(product, context={"request": request})

        return Response(read_serializer.data)
