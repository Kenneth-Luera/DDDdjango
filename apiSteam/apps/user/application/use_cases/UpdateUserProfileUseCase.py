class UpdateUserProfileUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, profile, data):
        return self.repository.update(profile, data)
