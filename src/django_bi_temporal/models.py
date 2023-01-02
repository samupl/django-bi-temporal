from datetime import datetime

from django.db import models
from django.utils.timezone import utc

from django_bi_temporal.queryset import BiTemporalManager

MAX_TIME = datetime.max.replace(tzinfo=utc)


class BiTemporalModel(models.Model):
    objects = BiTemporalManager()

    bitemp_valid_start_date: models.DateTimeField = models.DateTimeField()
    bitemp_valid_end_date: models.DateTimeField = models.DateTimeField(default=MAX_TIME)

    bitemp_sys_start_date: models.DateTimeField = models.DateTimeField()
    bitemp_sys_end_date: models.DateTimeField = models.DateTimeField(default=MAX_TIME)

    class Meta:
        abstract = True
