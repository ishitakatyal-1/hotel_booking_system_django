from rest_framework import serializers
from .models import Guests

class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = "__all__"