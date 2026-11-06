from django.db import models

class Spells(models.Model):
    name = models.CharField(max_length=200)  # Name of the card.
    id = models.IntegerField(primary_key=True)  # ID or Passcode of the card.
    type = models.CharField(max_length=200)  # The type of card you are viewing
    race = models.CharField(max_length=200)  # The card race which is officially called type for
                                            # Spell/Trap Cards (Field, Equip, Counter, etc).