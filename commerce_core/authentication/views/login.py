from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from commerce_core.users.serializers.user import UserReadSerializer

from ..serializers.login import LoginSerializer
from ..serializers.token import TokenSerializer


class LoginView(APIView):

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        return Response(
            {
                "authentication": TokenSerializer(user).data,
                "user": UserReadSerializer(user, context={
                    "request": request
                }).data,
            },
            status=status.HTTP_200_OK,
        )
