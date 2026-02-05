class ListUserUseCase:
    def __init__(self, user_reporistory):
        self.user_repository = user_reporistory

    def execute(self, requester):
        if not requester.is_authenticated:
            raise PermissionError("Usuario no autenticado")
        
        if not requester.is_superuser:
            raise PermissionError("No tienes permisos")
        
        return self.user_repository.get_all()    