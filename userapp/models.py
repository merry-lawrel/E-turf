from django.db import models

# Create your models here.
class Regdb(models.Model):
    u_name = models.CharField(max_length=20)
    u_password = models.CharField(max_length=20)
    mail  =  models.CharField(max_length=20)
    mob = models.CharField(max_length=20)

class Bookdb(models.Model):
    b_name = models.CharField(max_length=15, default='')
    b_password = models.CharField(max_length=15, default='')
    b_umail = models.CharField(max_length=40, default='')
    b_umob = models.CharField(max_length=40, default='')
    b_turf = models.CharField(max_length=40)
    b_price = models.CharField(max_length=10, default='')
    b_date = models.DateField()
    b_time = models.CharField(max_length=10)
    status = models.CharField(max_length=5, default = '0')

class Contactdb(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=20, default='')
    mobile = models.CharField(max_length=20, default='')
    c_message = models.TextField(max_length= 200)