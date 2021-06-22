from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Skyscraper
from .serializers import SkyscraperSerializer
from .permissions import IsOwnerOrReadOnly
from django.conf import settings

# Create your views here.

class SkyscraperList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Skyscraper.objects.all()
    serializer_class = SkyscraperSerializer

class SkyscraperDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Skyscraper.objects.all()
    serializer_class = SkyscraperSerializer

