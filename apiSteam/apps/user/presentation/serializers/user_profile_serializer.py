from rest_framework import serializers
from apiSteam.apps.user.infrastructure.models.user_profile_model import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "nickname",
            "age",
            "gender",
            "description",
            "avatar",
            "frame",
            "background",
        ]
class UpdateUserProfileSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=50, required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=False)
    description = serializers.CharField(required=False)
    avatar = serializers.URLField(required=False)
    frame = serializers.URLField(required=False)
    background = serializers.URLField(required=False)
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance