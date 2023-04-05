
from django.db import models

# Create your models here.
class appointment(models.Model):
    name        = models.CharField(max_length=100)
    age         = models.CharField(max_length=50)
    gender      = models.CharField(max_length=100)
    email       = models.EmailField(max_length=254)
    phonenumber = models.CharField(max_length=120)
    doctor      = models.CharField(max_length=100)
    datetime = models.DateTimeField(null=True,blank=True)
    # date        = models.DateField(auto_now_add=True)
    # time        = models.TimeField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    

            # {% comment %} age         = models.CharField(max_length=50)
            # gender      = models.CharField(max_length=100)
            # email       = models.EmailField(max_length=254)
            # doctor  {% endcomment %} 