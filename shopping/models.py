from django.db import models

# Create your models here.

class Shopping(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(1000) #cents
    
    
    
    def __str__(self):
        return self.name
