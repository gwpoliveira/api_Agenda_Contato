# contatos/views.py

from rest_framework import generics
from .models import Contato
from .serializers import ContatoSerializer

class ContatoListCreate(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ContatoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
