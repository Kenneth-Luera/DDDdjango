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