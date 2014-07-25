from ws.models import Set, Deck, Card
from ws.serializers import SetSerializer, DeckSerializer, CardSerializer
from rest_framework import generics

class SetList(generics.ListAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    
class SetDetail(generics.CreateAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    
class DeckList(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    
class DeckDetail(generics.CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    
class CardList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
class CardDetail(generics.CreateAPIView):
    queryset = Card.objects.all
    serializer_class = CardSerializer
    