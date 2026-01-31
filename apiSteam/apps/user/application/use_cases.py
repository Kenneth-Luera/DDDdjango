class CreateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

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
        return user


class ListUserUseCase:
    def __init__(self, user_reporistory):
        self.user_repository = user_reporistory

    def execute(self, requester):
        if not requester.is_authenticated:
            raise PermissionError("Usuario no autenticado")
        
        if not requester.is_superuser:
            raise PermissionError("No tienes permisos")
        
        return self.user_repository.get_all()    

class UpdateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, dto):
        user = self.user_repository.get_by_id(dto.user_id)
        if not user:
            raise ValueError("Usuario no encontrado")

        if dto.email:
            user.email = dto.email

        if dto.rol:
            user.change_role(dto.rol)

        if dto.account:
            user.account = dto.account

        return self.user_repository.update(user)