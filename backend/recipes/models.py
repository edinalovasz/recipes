from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=200
    )
    ingredients = models.CharField(
        max_length=200,
        blank=True
    )
    difficulty = models.IntegerField(
        choices=[
            (1, "EASY"),
            (2, "INTERMEDIATE"),
            (3, "HARD")
        ]
    )
    favourite = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True
    )


