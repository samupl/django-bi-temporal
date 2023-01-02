from django.db import models

from django_bi_temporal.models import BiTemporalModel


class Employee(models.Model):
    name = models.CharField(max_length=128)


class Salary(BiTemporalModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
