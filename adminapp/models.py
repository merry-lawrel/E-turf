from django.db import models

# Create your models here.
class Catdb(models.Model):
    cat_name = models.CharField(max_length=10)

class  Turfdb(models.Model):
    t_name = models.CharField(max_length=40)
    t_location = models.CharField(max_length=40)
    t_cat = models.CharField(max_length=30, default='')
    t_price = models.CharField(max_length=10)
    t_image  = models.ImageField(upload_to='Turf')

class Mandb(models.Model):
    m_name = models.CharField(max_length=20)
    m_password = models.CharField(max_length=20)
    m_mail = models.CharField(max_length=20)
    m_turf = models.CharField(max_length=40)
    m_image = models.ImageField(upload_to='Manager')