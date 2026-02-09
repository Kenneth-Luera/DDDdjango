from apiSteam.apps.library.infrastructure.models.library_model import Library, LibraryGame
from apiSteam.apps.library.domain.respositories.library_repository import LibraryRepository


class DjangoLibraryRepository(LibraryRepository):

    def get_library_by_user(self, user_id):
        return Library.objects.get(user_id=user_id)

    def add_game(self, library_id, game_id):
        return LibraryGame.objects.create(
            library_id=library_id,
            game_id=game_id
        )

    def remove_game(self, library_id, game_id):
        return LibraryGame.objects.filter(
            library_id=library_id,
            game_id=game_id
        ).delete()

    def list_games(self, library_id):
        return LibraryGame.objects.filter(library_id=library_id)
