from rest_framework import serializers
from .models import Reservation, ConfirmationLogs, BillingDraft, BillingPayment

class ReservationSerializer(serializers.ModelSerializer):
    model = Reservation
    fields = ('guest_id', 'num_people', 'check_indate', 'check_outdate','details','confirmation_status')

class ConfirmationLogsSerializer(serializers.ModelSerializer):
    model = ConfirmationLogs
    fields = "__all__"

class BillingDraftSerializer(serializers.ModelSerializer):
    model = BillingDraft
    fields = "__all__"

class BillingPaymentSerialzier(serializers.ModelSerializer):
    model = BillingPayment
    fields = "__all__"