from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user')
        #add product and quantity