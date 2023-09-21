from django.db import models
from urllib.parse import urljoin
from django.conf import settings

class Todo(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=255)
    DATE = models.DateField()
    DUE = models.DateField()
    FEE = models.DecimalField(max_digits=10, decimal_places=2)
    CONTACT_NO = models.CharField(max_length=20)
    EMAIL = models.EmailField()
    STATUS = models.CharField(max_length=50)
    
    def __str__(self):
        return self.NAME


