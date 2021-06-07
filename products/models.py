from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Product(models.Model):
    name = models.CharField(null=False,blank=False,unique=True,max_length=255)
    price = models.FloatField(null=False,blank=False)
    
    def __str__(self):
        return self.name

class users(models.Model):
    name = models.CharField(null=False,blank=False,max_length=255)
    def __str__(self):
        return self.name

class cart(models.Model):
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False,blank=False)
    total_price = models.FloatField(null=False,blank=False)