from django.db import models

# Create your models here.



class farmers(models.Model):
    owner_name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    farmer_name = models.CharField(max_length=50)
    time = models.TimeField()
    rate = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    disel = models.CharField(max_length=50)


    class Meta:
        db_table = 'farmers'

    
