from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    nickname = models.CharField(max_length=50, unique=True, null=True, blank=True)
    age = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    avatar = models.URLField(
        default="https://i.pinimg.com/236x/d4/74/1c/d4741cb779ddec6509ca1ae0cb137a7d.jpg"
    )
    frame = models.URLField(
        default="https://cdn.fastly.steamstatic.com/steamcommunity/public/images/items/860950/6e1b5f5977036a189465f5455f2c54722c12883d.png"
    )
    background = models.URLField(
        default="https://w.wallhaven.cc/full/9o/wallhaven-9o687w.png"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Profile of {self.user.username}"
