from django.core import serializers
from .models import RoomsCategory, RoomsName, RoomsBookedStatus

class RoomsCategory_Serializers(serializers.ModelSerializer):
    model = RoomsCategory
    fields = "__all__"

class RoomsName_Serialzier(serializers.ModelSerializer):
    model = RoomsName
    fields = "__all__"

class RoomsBookedStatus_Serializer(serializers.ModelSerializer):
    model = RoomsBookedStatus
    fields = "__all__"