from rest_framework import serializers
from ws.models import Set, Deck, Card

class SetSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Set
        fields = ('name', 'numofdecks')
        
class DeckSerializer(serializers.ModelSerializer):
    #set_id = serializers.Field(source='deck.set_id')
    class Meta:
        model = Deck
        fields = ('set', 'name', 'numofcards')
        
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('deck', 'word', 'pronunciation', 'definition', 'example')