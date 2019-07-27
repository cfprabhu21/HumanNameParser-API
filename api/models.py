from django.db import models

# Create your models here.
class MapFlag(models.Model):
    flag = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    # def __str__(self):
    #     return self.id, str(self.status)
