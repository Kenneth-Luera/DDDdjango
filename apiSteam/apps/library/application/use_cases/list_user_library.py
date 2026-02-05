class ListUserLibraryUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        return self.repository.list_by_user(user)
