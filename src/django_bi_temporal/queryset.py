from django.db.models import QuerySet
from django.db.models.manager import Manager


class BiTemporalQuerySet(QuerySet):
    pass


class BiTemporalManager(Manager):
    def get_queryset(self):
        return BiTemporalQuerySet(self.model, using=self._db)
