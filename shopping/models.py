from django.db import models

# Create your models here.

class Shopping(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0) #cents
    
    
    
    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price/100)
