from django.db import models

# Create your models here.

class Deaths(models.Model):
    age = models.IntegerField()
    case_number = models.CharField(max_length=50)
    cause_of_death = models.CharField(max_length=1000)
    death_city = models.CharField(max_length=50)
    res_city = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.case_number