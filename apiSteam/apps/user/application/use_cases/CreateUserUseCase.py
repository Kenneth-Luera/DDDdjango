from apiSteam.apps.user.infrastructure.repositories.DjangoUserProfileRepository import DjangoUserProfileRepository

class CreateUserUseCase:
    def __init__(self, user_repository, profile_repository=None):
        self.user_repository = user_repository
        self.profile_repository = profile_repository or DjangoUserProfileRepository()

    def execute(self, username, email, password):
        if self.user_repository.exists(username=username):
            raise ValueError("Username already exists")
        if self.user_repository.exists(email=email):
            raise ValueError("Email already exists")
        if not username or not email or not password:
            raise ValueError("Missing required fields")
        
        user = self.user_repository.create(
            username=username,
            email=email,
            password=password,
            rol="USER",
            account="ACTIVE"
        )

        self.profile_repository.create(user)

        return user
