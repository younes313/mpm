from django.db import models
from django.contrib.auth.models import User


from company.models import Company


# Create your models here.


class Funder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 20)


class History(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    funder = models.ForeignKey(Funder, on_delete=models.CASCADE)
    money = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    public_or_specefic = models.CharField(max_length = 10)
    help_or_contribute = models.CharField(max_length = 10)
