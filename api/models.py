from django.db import models

# Create your models here.
class MapFlag(models.Model):
    flag = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
