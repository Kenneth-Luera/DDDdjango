from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from apiSteam.apps.games.application.use_cases.create_games import CreateGameUseCase
from apiSteam.apps.games.application.use_cases.list_games import ListGamesUseCase
from apiSteam.apps.games.application.use_cases.get_game_detail import GetGameDetailUseCase
from apiSteam.apps.games.infrastructure.repositories.django_game_repository import DjangoGameRepository
from apiSteam.apps.games.presentation.serializers.game_serializer import GameSerializer


class GameListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        repo = DjangoGameRepository()
        use_case = ListGamesUseCase(repo)
        games = use_case.execute()

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        repo = DjangoGameRepository()
        use_case = CreateGameUseCase(repo)
        game = use_case.execute(**serializer.validated_data)

        return Response(GameSerializer(game).data, status=status.HTTP_201_CREATED)


class GameDetailView(APIView):

    def get(self, request, game_id):
        repo = DjangoGameRepository()
        use_case = GetGameDetailUseCase(repo)
        game = use_case.execute(game_id)

        return Response(GameSerializer(game).data)

    def put(self, request, game_id):
        repo = DjangoGameRepository()
        use_case = GetGameDetailUseCase(repo)
        game = use_case.execute(game_id)

        serializer = GameSerializer(game, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_game = repo.update(game, **serializer.validated_data)

        return Response(GameSerializer(updated_game).data, status=status.HTTP_200_OK)

    def delete(self, request, game_id):
        repo = DjangoGameRepository()
        game = repo.get_by_id(game_id)
        game.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
