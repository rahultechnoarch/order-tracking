from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_Price = models.CharField(max_length=10)
    custname = models.CharField(max_length=50)
    custemail = models.CharField(max_length=50)
    custnumber = models.CharField(max_length=12)
    custaddress = models.CharField(max_length=100)
    order_Time = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Customer Name: " + self.custname
