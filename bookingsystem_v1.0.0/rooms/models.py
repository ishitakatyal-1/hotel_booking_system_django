from django.db import models
from mealplans.models import MealPlans
from roomscategory.models import RoomsCategory
from mealplans.models import MealPlans

# Create your models here.
class CostMealCategoryPlan(models.Model):
    s_no = models.AutoField(primary_key = True)
    roomscategory_id = models.ForeignKey(RoomsCategory, on_delete=models.CASCADE)
    mealplans_id = models.ForeignKey(MealPlans, on_delete =  models.CASCADE)
    cost_in_rs = models.IntegerField()
    descr = models.TextField()

    class Meta:
        db_table = "cost_meal_category_plan"