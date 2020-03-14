from django.shortcuts import render
from .models import RoomsCategory, RoomsName, RoomsBookedStatus
from .serializers import RoomsCategory_Serializers, RoomsName_Serialzier, RoomsBookedStatus_Serializer
from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your tests here.
class RoomsCategoryView(APIView):

    def post(self, request):
        ser = RoomsCategory_Serializers(data = request.data)
        if ser.is_valid(raise_exception = True):
            ser.save()
            for i in request.data['num_rooms']:
                name = request.data['category_name'][0]+i
                print(name)
                if name not in RoomsName['room_name']:
                    RoomsName.objects.create('room_name' = name)
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request):
        data = RoomsCategory.objects.all()
        ser = RoomsCategory_Serializers(data, many = True)
        return Response(ser.data) 

class RoomsNameView(APIView):
    def get(self, request):
        data = RoomsName.objects.all()
        ser = RoomsName_Serialzier(data, many= True)
        return Response(ser.data)

class RoomsBookedStatusView(APIView):
    def get(self, request):
        data = RoomsBookedStatus.objects.filter(booked_status = True).all()
        ser = RoomsBookedStatus_Serializer(data, many=True)
        return Response(ser.data)


