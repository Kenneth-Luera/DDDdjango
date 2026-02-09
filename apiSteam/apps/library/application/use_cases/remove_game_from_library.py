from apiSteam.apps.library.infrastructure.repositories.django_library_repository import DjangoLibraryRepository


class RemoveGameFromLibraryUseCase:

    def __init__(self):
        self.repo = DjangoLibraryRepository()

    def execute(self, user_id, game_id):
        library = self.repo.get_library_by_user(user_id)
        return self.repo.remove_game(library.id, game_id)
