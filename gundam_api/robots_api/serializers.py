from rest_framework import serializers
from .models import Gundam

class GundamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gundam
        fields = ('id', 'name', 'price', 'shippingCost', 'shippingDate', 'image')