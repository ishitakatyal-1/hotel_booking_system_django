from django.db import models

# Create your models here.
class MealPlans(models.Model):
    s_no = models.AutoField(primary_key = True)
    plan_name = models.CharField(max_length=100)
    alias_name = models.CharField(max_length=1)
    descr = models.TextField()
    date_added = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "meal_plans"