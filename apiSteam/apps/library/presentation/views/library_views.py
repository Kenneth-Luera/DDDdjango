from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apiSteam.apps.library.application.use_cases.add_game_to_library import AddGameToLibraryUseCase
from apiSteam.apps.library.application.use_cases.list_user_library import ListUserLibraryUseCase
from apiSteam.apps.library.application.use_cases.remove_game_from_library import RemoveGameFromLibraryUseCase
from apiSteam.apps.library.presentation.serializers.library_serializer import LibraryGameSerializer


class UserLibraryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        use_case = ListUserLibraryUseCase()
        games = use_case.execute(request.user.id)
        serializer = LibraryGameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        game_id = request.data.get("game_id")
        use_case = AddGameToLibraryUseCase()
        library_game = use_case.execute(request.user.id, game_id)
        serializer = LibraryGameSerializer(library_game)
        return Response(serializer.data)

    def delete(self, request):
        game_id = request.data.get("game_id")
        use_case = RemoveGameFromLibraryUseCase()
        use_case.execute(request.user.id, game_id)
        return Response({"detail": "Game removed from library"})
