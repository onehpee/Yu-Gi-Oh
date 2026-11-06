from django.db import models

class Monsters(models.Model):
    name = models.CharField(max_length=200) # Name of the card.
    id  = models.IntegerField(primary_key=True) # ID or Passcode of the card.
    type = models.CharField(max_length=200) # The type of card you are viewing
                                            # (Normal Monster, Effect Monster,
                                            # Synchro Monster, Spell Card, Trap Card, etc.).
    atk = models.IntegerField() # The ATK value of the card.
    defense = models.IntegerField() # The DEF value of the card.
    level = models.IntegerField() # The Level/RANK of the card.
    race = models.CharField(max_length=200) # The card race which is officially called type
                                            # (Spellcaster, Warrior, Insect, etc).
    attribute = models.CharField(max_length=200) # The attribute of the card.

