from apiSteam.apps.library.infrastructure.models.library_model import Library
from apiSteam.apps.library.domain.respositories.library_repository import LibraryRepository


class DjangoLibraryRepository(LibraryRepository):

    def add_game(self, user, game):
        return Library.objects.create(user=user, game=game)

    def list_by_user(self, user):
        return Library.objects.filter(user=user)

    def remove_game(self, user, game):
        Library.objects.filter(user=user, game=game).delete()
