from rest_framework import serializers
from apiSteam.apps.games.infrastructure.models.game_model import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
