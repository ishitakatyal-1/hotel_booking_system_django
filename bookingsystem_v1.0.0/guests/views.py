from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Guests
from .serializers import GuestsSerializer
import os
import shutil

# Create your views here.
class GuestsView(APIView):
    def post(self, request):
        ser = GuestsSerializer(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            a = str(request.data['s_no'])
            print(a)
            path = os.path.join("media", a)
            if not os.path.exists():
                os.mkdirs(path)
                shutil.move("media", a)
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request):
        data = Guests.objects.all()
        ser = GuestsSerializer(data, many= True)
        return Response(ser.data)

class GuestDateFiilterView(APIView):
    def get(self, request):
        obj = Guests.objects.filter(date_added = request.data['date_added']).all()
        ser = GuestsSerializer(data, many= True)
        return Response(ser.data)