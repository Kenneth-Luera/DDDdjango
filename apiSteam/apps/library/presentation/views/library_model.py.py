from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apiSteam.apps.library.application.use_cases.add_game_to_library import AddGameToLibraryUseCase
from apiSteam.apps.library.application.use_cases.list_user_library import ListUserLibraryUseCase
from apiSteam.apps.library.application.use_cases.remove_game_from_library import RemoveGameFromLibraryUseCase
from apiSteam.apps.library.infrastructure.repositories.django_library_repository import DjangoLibraryRepository
from apiSteam.apps.library.presentation.serializers.library_serializer import LibrarySerializer
from apiSteam.apps.games.infrastructure.models.game_model import Game  # suponiendo que existe


class UserLibraryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        repo = DjangoLibraryRepository()
        use_case = ListUserLibraryUseCase(repo)
        library = use_case.execute(request.user)

        serializer = LibrarySerializer(library, many=True)
        return Response(serializer.data)

    def post(self, request):
        game_id = request.data.get("game_id")
        game = Game.objects.get(id=game_id)

        repo = DjangoLibraryRepository()
        use_case = AddGameToLibraryUseCase(repo)
        item = use_case.execute(request.user, game)

        return Response(LibrarySerializer(item).data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        game_id = request.data.get("game_id")
        game = Game.objects.get(id=game_id)

        repo = DjangoLibraryRepository()
        use_case = RemoveGameFromLibraryUseCase(repo)
        use_case.execute(request.user, game)

        return Response({"message": "Game removed from library"}, status=status.HTTP_200_OK)
