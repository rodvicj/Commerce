from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from commerce_core.auctions.serializers.address import AddressSerializer

from ..models import Address

# from rest_framework.parsers import FormParser, MultiPartParser
# from rest_framework.response import Response

# from thenewboston.general.permissions import IsObjectOwnerOrReadOnly


class AddressViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser,)
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.none()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Address.objects.filter(owner=self.request.user)
