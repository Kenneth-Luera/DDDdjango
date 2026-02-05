from rest_framework import serializers
from apiSteam.apps.library.infrastructure.models.library_model import Library


class LibrarySerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source="game.title", read_only=True)

    class Meta:
        model = Library
        fields = ["id", "game", "game_title", "added_at"]
