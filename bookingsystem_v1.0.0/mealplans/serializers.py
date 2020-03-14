from rest_framework import serializers
from .models import MealPlans

class MealPlans_Serializers(serializers.ModelSerializer):
    class Meta:
        model = MealPlans
        fields = "__all__"