from apiSteam.apps.games.infrastructure.models.game_model import Game
from apiSteam.apps.games.domain.repositories.game_repository import GameRepository


class DjangoGameRepository(GameRepository):

    def create(self, **data):
        return Game.objects.create(**data)

    def list_all(self):
        return Game.objects.filter(status="ACTIVE")

    def get_by_id(self, game_id):
        return Game.objects.get(id=game_id)

    def update(self, game, **data):
        for key, value in data.items():
            setattr(game, key, value)
        game.save()
        return game
