from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apiSteam.apps.user.application.use_cases import CreateUserUseCase
from apiSteam.apps.user.application.use_cases import ListUserUseCase
from apiSteam.apps.user.application.use_cases import UpdateUserUseCase
from apiSteam.apps.user.infrastructure.repositories import DjangoUserRepository
from apiSteam.apps.user.presentation.serializers import UserSerializer, UpdateUserSerializer


class UserCreateView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = CreateUserUseCase(DjangoUserRepository())
        user = use_case.execute(**serializer.validated_data)

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