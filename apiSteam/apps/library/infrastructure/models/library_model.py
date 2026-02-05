from django.db import models
from django.conf import settings


class Library(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="library"
    )

    game = models.ForeignKey(
        "games.Game",
        on_delete=models.CASCADE,
        related_name="libraries"
    )

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "game")

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"
