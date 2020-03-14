from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MealPlans
from .serializers import MealPlans_Serializers

# Create your views here.
class MealPlansView(APIView):

    def post(self, request):
        ser = MealPlans_Serializers(data = request.data)
        if ser.is_valid(raise_exception = True):
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request):
        data = MealPlans.objects.all()
        ser = MealPlans_Serializers(data, many=True)
        return Response(ser.data)