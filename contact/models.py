from django.db import models

from home.models import IndexSendEmail
# Create your models here.

class FeedBack(models.Model):
    Name =  models.CharField(max_length=100,null=False)
    Email = models.EmailField(null=False)
    Star = models.IntegerField(null = False)
    Number =  models.CharField(default='' , max_length=15)
    WriteMessage = models.TextField(max_length=100)
    
    
    def __str__(self):
        return f"{self.id},{self.Name},{self.Email}"
    
    
class contactEmail(models.Model):
    Email = models.EmailField(null=False)
    
    def __str__(self):
        return f"{self.id},{self.Email}"
    

    
