from django.contrib.auth import get_user_model
from rest_framework import serializers
from apiSteam.apps.user.application.dto import UpdateUserDTO

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    rol = serializers.ChoiceField(choices=User.ROL_CHOICES, required=False)
    state_account = serializers.ChoiceField(choices=User.STATE_ACCOUNT_CHOICES, required=False)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    def update(self, instance, validated_data):
        dto = UpdateUserDTO(
            user_id=instance.id,
            email=validated_data.get('email', None),
            rol=validated_data.get('rol', None),
            state_account=validated_data.get('state_account', None),
            balance=validated_data.get('balance', None)
        )
        for field, value in dto.__dict__.items():
            if value is not None and field != 'user_id':
                setattr(instance, field, value)
        instance.save()
        return instance