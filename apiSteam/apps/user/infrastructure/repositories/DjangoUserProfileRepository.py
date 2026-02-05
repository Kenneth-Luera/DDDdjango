from apiSteam.apps.user.infrastructure.models.user_profile_model import UserProfile
from apiSteam.apps.user.domain.repositories.user_profile_repository import UserProfileRepository


class DjangoUserProfileRepository(UserProfileRepository):

    def create(self, user):
        return UserProfile.objects.create(user=user)

    def get_by_user(self, user):
        profile, created = UserProfile.objects.get_or_create(user=user)
        return profile

    def update(self, profile, data):
        for key, value in data.items():
            setattr(profile, key, value)
        profile.save()
        return profile
