from django.db import models
from django.contrib.postgres.fields import JSONField
from guests.models import Guests

# Create your models here.
class Reservation(models.Model):
    s_no = models.AutoField(primary_key=True)
    guests_id = models.ForeignKey(Guests, on_delete=models.CASCADE)
    num_people = models.IntegerField()
    num_rooms = models.IntegerField()
    check_indate = models.DateField()
    check_outdate =  models.DateField()
    duration = models.IntegerField()
    details = models.TextField()
    #includes the rooms as per the guests' desires
    added_date = models.DateTimeField(auto_now = True)
    confirmation_status = models.BooleanField(default = False)
    
    class Meta:
        db_table = "reservation"

class ConfirmationLogs(models.Model):
    s_no = models.AutoField(primary_key = True)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    log_mode = models.CharField(max_length =20)
    #log mode is either phone call or email or whatsapp or messenger
    message = models.TextField()
    positive = models.BooleanField(default=False)
    log_details = models.TextField()
    #call duration and email sent on particular date 
    added_date = models.DateTimeField(auto_now=True)
    num_people = models.IntegerField()
    room_alotted = JSONField()
    """
        {
            "rooms with plans and dates" : [
                {
                    "room_name" : "B1",
                    "plan_id" : "1",
                    "from_date": "26-02-2020",
                    "to_date": "28-20-2020",
                },
                {
                    "room_name" : "S2",
                    "plan_id" : "2",
                    "from_date": "26-02-2020",
                    "to_date": "30-02-2020", 
                },
            ]
        }
    in case of partial booking or payments with multiple checkouts
    """
    class Meta:
        db_table = "confirmation_logs"

class BillingDraft(models.Model):
    s_no = models.AutoField(primary_key = True)
    confirmation_log_id = models.ForeignKey(ConfirmationLogs, on_delete=models.CASCADE)
    total_bill = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add = True)
    paid = models.BooleanField(default = False)
    
    class Meta:
        db_table = "billing_draft"

class BillingPayment(models.Model):
    s_no = models.AutoField(primary_key=True)
    billing_draft_id = models.ForeignKey(BillingDraft, on_delete = models.CASCADE)
    mode = models.CharField(max_length = 100)
    payment_date = models.DateTimeField(auto_now= True)

    class Meta:
        db_table = "billing_payment"
    