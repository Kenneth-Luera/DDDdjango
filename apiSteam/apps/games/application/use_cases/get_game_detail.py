class GetGameDetailUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, game_id):
        return self.repository.get_by_id(game_id)
