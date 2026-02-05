class CreateUserProfileUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        return self.repository.create(user)
