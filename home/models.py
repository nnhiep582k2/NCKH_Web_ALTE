from django.db import models


class IndexSendEmail(models.Model):
    Email = models.EmailField(null=False)
    
    def __str__(self):
        return f"{self.id},{self.Email}"