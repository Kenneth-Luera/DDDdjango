from rest_framework import serializers
from apiSteam.apps.library.infrastructure.models.library_model import LibraryGame


class LibraryGameSerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source="game.title", read_only=True)

    class Meta:
        model = LibraryGame
        fields = ["id", "game", "game_title", "added_at", "hours_played", "is_favorite"]
