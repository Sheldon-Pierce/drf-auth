from django.shortcuts import render
from django.views.generic import ListView
from .models import Games
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializer import GamesSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class GamesList(ListAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = GamesSerializer
    queryset = Games.objects.all()


class GamesDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

