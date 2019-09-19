from django.db import models
from django.contrib.auth.models import User



class Company(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    stock_percent = models.FloatField()
    needed_fee = models.IntegerField()
    remained_fee = models.IntegerField(blank=True)
    # on_demand = first phase and need money
    # call = gain enough money and we call them
    # released 
    status = models.CharField(max_length=10, default='on_demand')

    # def save(self, *args, **kwargs):
    #     super(Company, self).save(*args, **dic)
    #     # self.remained_fee = self.needed_fee
        # self.save()

    def __str__(self):
        return self.name

class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField()
