class AddGameToLibraryUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, game):
        return self.repository.add_game(user, game)
