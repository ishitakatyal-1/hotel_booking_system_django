from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Guests(models.Model):
    s_no = models.AutoField(primary_key=True)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    #address = models.AddressField(max_length = 100)
    address = JSONField()
    phone = models.CharField(max_length= 15)
    email = models.EmailField(max_length= 100)
    id_proof = models.FileField(upload_to = "media/", null = True)
    date_added = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "guests"