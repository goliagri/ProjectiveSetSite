from django.db import models

# Create your models here.

class Card(models.Model):
    points = models.CharField(max_length = 30) #binary encoding of points present on card in reading order, eg '010100' has a point in the top right and center right
    loc = models.CharField(max_length = 30) #code for where the card is currently located, eg board, deck, discard, etc.
    #currently meaningful vals are 'deck' 'play' 'discard'
    selected = models.BooleanField() # is the card currently selected by the player

class PlayPosition(models.Model):
    card = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL) # Which card is currently at this position
    pos_id = models.IntegerField() # Where is this position in the ordering