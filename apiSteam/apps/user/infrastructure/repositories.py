from django.contrib.auth import get_user_model

User = get_user_model()

class DjangoUserRepository:
    def create_user(self, *, username, email, password, rol, account):
        user = User(
            username=username,
            email=email,
            rol=rol,
            account=account
        )
        user.set_password(password)
        user.save()
        return user

    def get_all(self):
        return User.objects.all()
