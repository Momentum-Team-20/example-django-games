from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=255)
    number_of_players = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
