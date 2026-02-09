from django.db import models
from django.conf import settings


class Library(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="library"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Library of {self.user.username}"


class LibraryGame(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name="games"
    )
    game = models.ForeignKey(
        "games.Game",
        on_delete=models.CASCADE,
        related_name="library_entries"
    )
    added_at = models.DateTimeField(auto_now_add=True)
    hours_played = models.FloatField(default=0)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        unique_together = ("library", "game")

    def __str__(self):
        return f"{self.library.user.username} - {self.game.title}"
