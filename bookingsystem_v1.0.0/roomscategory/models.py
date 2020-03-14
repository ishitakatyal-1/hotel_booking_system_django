from django.db import models

# Create your models here.
class RoomsCategory(models.Model):
    s_no = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length=100)
    num_rooms = models.IntegerField()
    descr = models.TextField()
    added_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "rooms_category"

class RoomsName(models.Model):
    s_no = models.AutoField(primary_key = True)
    room_name = models.CharField(max_length = 5)

    class Meta:
        db_table = "rooms_name"

class RoomsBookedStatus(models.Model):
    s_no = models.AutoField(primary_key = True)
    room_id = models.ForeignKey(RoomsName, on_delete = models.CASCADE)
    booked_status = models.BooleanField(default = False)

    class Meta:
        db_table = "rooms_booked_status"