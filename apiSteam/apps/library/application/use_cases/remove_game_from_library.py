class RemoveGameFromLibraryUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, game):
        self.repository.remove_game(user, game)
