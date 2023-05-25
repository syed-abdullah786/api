from django.shortcuts import render
from .models import Items
from .serializers import ItemSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ItemViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer