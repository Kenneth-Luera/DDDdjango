from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apiSteam.apps.user.application.use_cases.get_user_profile import GetUserProfileUseCase
from apiSteam.apps.user.infrastructure.repositories.DjangoUserProfileRepository import DjangoUserProfileRepository
from apiSteam.apps.user.application.use_cases.UpdateUserProfileUseCase import UpdateUserProfileUseCase
from apiSteam.apps.user.presentation.serializers.user_profile_serializer import UserProfileSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        repo = DjangoUserProfileRepository()
        use_case = GetUserProfileUseCase(repo)
        profile = use_case.execute(request.user)

        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        repo = DjangoUserProfileRepository()
        get_use_case = GetUserProfileUseCase(repo)
        profile = get_use_case.execute(request.user)

        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        update_use_case = UpdateUserProfileUseCase(repo)
        profile = update_use_case.execute(profile, serializer.validated_data)

        return Response(UserProfileSerializer(profile).data, status=status.HTTP_200_OK)
    
    def post(self, request):
        repo = DjangoUserProfileRepository()
        get_use_case = GetUserProfileUseCase(repo)
        profile = get_use_case.execute(request.user)

        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        update_use_case = UpdateUserProfileUseCase(repo)
        profile = update_use_case.execute(profile, serializer.validated_data)

        return Response(UserProfileSerializer(profile).data, status=status.HTTP_200_OK)
