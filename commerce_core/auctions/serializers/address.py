from rest_framework import serializers

from ..models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"
        # NOTE: read_only_fields prevents modification of the included fields;
        read_only_fields = (
            "created_date",
            "modified_date",
            "owner",
        )

    # def create(self, validated_data):
    #     request = self.context.get("request")
    #     return Address.objects.create(**validated_data, owner=request.user)
