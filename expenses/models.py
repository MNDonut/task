from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=255)
    amount = models.FloatField(validators=[MinValueValidator(0.01)])
    date = models.DateField()
    # it is mentioned that there should be only User and Expense entities, thus I don't create another ExpenseCategoryType entity
    # also don't set choices as it's unknown if it's a static list
    category = models.CharField(max_length=63)
