from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apiSteam.apps.user.application.use_cases.CreateUserUseCase import CreateUserUseCase
from apiSteam.apps.user.application.use_cases.ListUserUseCase import ListUserUseCase
from apiSteam.apps.user.application.use_cases.UpdateUserUseCase import UpdateUserUseCase
from apiSteam.apps.user.application.use_cases.UpdateUserLocationUseCase import UpdateUserLocationUseCase


from apiSteam.apps.user.infrastructure.repositories.DjangoUserRepository import DjangoUserRepository
from apiSteam.apps.user.presentation.serializers.user_serializer import UserSerializer, UpdateUserSerializer

from apiSteam.apps.user.application.utils.ip import get_client_ip


class UserCreateView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repo = DjangoUserRepository()
        use_case = CreateUserUseCase(repo)
        user = use_case.execute(**serializer.validated_data)

        ip = get_client_ip(request)
        geo_use_case = UpdateUserLocationUseCase()
        geo_use_case.execute(user, ip)

        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class UsersViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['get', 'put']

    def list(self, request):
        use_case = ListUserUseCase(DjangoUserRepository())
        users = use_case.execute(request.user)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = serializer.to_dto(user_id=pk)

        use_case = UpdateUserUseCase(DjangoUserRepository())
        user = use_case.execute(dto)

        return Response(
            UserSerializer(user).data,
            status=status.HTTP_200_OK
        )