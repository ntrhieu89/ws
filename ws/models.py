from django.db import models

# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    numofdecks = models.IntegerField(blank=False, default=0)
    createdtime = models.DateTimeField(auto_now_add=True)
    
class Deck(models.Model):
    set = models.ForeignKey(Set, related_name="decks")
    
    name = models.CharField(max_length=100, blank=False, default='')
    numofcards = models.IntegerField(blank=False, default = 0)
    createdtime = models.DateTimeField(auto_now_add=True)
    
class Card(models.Model):
    deck = models.ForeignKey(Deck, related_name='cards')
    
    word = models.CharField(max_length=100, blank=False, default='')
    pronunciation = models.CharField(max_length=100, blank=True, default='')
    definition = models.CharField(max_length=1000, blank=False, default='')
    example = models.CharField(max_length=1000, blank=False, default='')
    createdtime = models.DateTimeField(auto_now_add=True)