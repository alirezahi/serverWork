import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


# Create your models here.
class Name(models.Model):
    name_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name_text
    class Meta:
        db_table = "Names"
        ordering = [
            '-score'
        ]

