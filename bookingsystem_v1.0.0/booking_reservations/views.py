from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation, ConfirmationLogs, BillingDraft, BillingPayment
from .serializer import ( ReservationSerializer,ConfirmationLogsSerializer, 
        BillingDraftSerializer, BillingPaymentSerialzier)
from django.db.models import F
from datetime import date
from datetime import timedelta

# Create your views here.
class ReservationPlanningView(APIView):
    def post(self, request):
        ser = ReservationSerializer(data = request.data)
        if ser.is_valid(raise_exception= True):
            ser.save()
            people = request.data['num_people']
            if people%2 == 0:
                request.data['num_rooms'] = people//2
            else:
                request.data['num_rooms'] = people//2 + 1
            date_in = request.date['check_indate']
            date_out = request.date['check_outdate']
            num_days = (date_out - date_in).days
            ser.data['duration'] = num_days
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request):
        data = Reservation.objects.values(
            's_no',
            'num_people', 
            'num_rooms', 
            'check_indate', 
            'check_outdate', 
            'duration',
            'details',
            'confirmation_status',
            guest_name = F('guest_id__fname'+' '+'guest_id__lname')
        )
        return Response(data)

class ReservationStatusFilterView(APIView):
    def get(self, request):
        obj1 = Reservation.objects.filter(confirmation_status = request.data['confirmation_status']).all()
        return Response(obj1)

class ConfirmationLogsView(APIView):
    def post(self, request):
        ser = ConfirmationLogsSerializer(data = request.data, partial=True)
        if ser.is_valid(raise_exception=True):
            ser.save()
            Reservation.objects.filter(s_no = ConfirmationLogs.objects.values('reservation_id')).update(confirmation_status = True))
            ConfirmationLogs.objects.filter(reservation_id = request.data['reservation_id']).update(positive = True)
            BillingDraft.objects.create(confirmation_log_id = ConfirmationLogs.objects.values('s_no'))
            b = request.data['room_alotted']['rooms with plans and dates']
            print(b)
            bill = 0
            for i in b:
                print(i)
                f = i['from_date']
                l = i['to_date']
                dur = (l-f).days
                cost_per_day = F('i["plan_id"]__cost_in_rs')
                total_cost = dur*cost_per_day
                bill += total_cost
            total_bill = bill
            BillingDraft.objects.create(total_bill = total_bill)    
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request):
        data = ConfirmationLogs.objects.all()
        ser = ConfirmationLogsSerializer(data, many=True)
        return Response(ser.data) 

class ConfirmationLogsFilterView(APIView):
    def get(self, request):
        data = ConfirmationLogs.objects.filter(positive = True).all()
        ser = ConfirmationLogsSerializer(data, many = True)
        return Response(ser.data)

class BillingDraftView(APIView):
    def get(self, request):
        data = BillingDraft.objects.all()
        ser = BillingDraftSerializer(data, many= True)
        return Response(ser.data)

class BillingPaymentView(APIView):
    def post(self, request):
        ser = BillingPaymentSerialzier(data = request.data)
        if ser.is_valid(raise_exception = True):
            ser.save()
            BillingDraft.objects.filter(s_no = BillingPayment.objects.values('billing_draft_id')).update(paid = True)
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request):
        data = BillingPayment.objects.all()
        ser = BillingPaymentSerialzier(data, many=True)
        return Response(ser.data)

