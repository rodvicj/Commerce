from rest_framework import serializers

from ..models import CartProduct, Product
from ..models.product import ActivationStatus
from .user import UserReadSerializer


class ProductReadSerializer(serializers.ModelSerializer):
    seller = UserReadSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = (
            "created_date",
            "modified_date",
            "seller",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        product = super().create({
            **validated_data,
            "seller": request.user,
        })

        return product

    def update(self, instance, validated_data):
        activation_status = validated_data.get("activation_status")

        if (
            activation_status and instance.activation_status == ActivationStatus.ACTIVE and
            activation_status == ActivationStatus.DRAFT
        ):
            CartProduct.objects.filter(product=instance).delete()

        return super().update(instance, validated_data)
