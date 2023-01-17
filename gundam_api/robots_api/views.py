from django.shortcuts import render
from rest_framework import generics
from .serializers import GundamSerializer
from .models import Gundam

# Create your views here.

class GundamList(generics.ListCreateAPIView):
    queryset = Gundam.objects.all().order_by('id')
    serializer_class = GundamSerializer

class GundamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gundam.objects.all().order_by('id')
    serializer_class = GundamSerializer