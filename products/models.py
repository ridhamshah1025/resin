from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(null=False,blank=False,unique=True,max_length=255)
    price = models.FloatField(null=False,blank=False)
    
    def __str__(self):
        return self.name