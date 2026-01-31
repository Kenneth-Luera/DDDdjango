class UserService:
    @staticmethod
    def get_user_by_username(username):
        from apiSteam.apps.user.infrastructure.models import User
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None