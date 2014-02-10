from django.db import models

class Software(models.Model):
    
    name = models.CharField(max_length=50)
    url = models.URLField()
    category = models.CharField(max_length=80)
    additional_category = models.CharField(max_length=50)
    license_model = models.CharField(max_length=40)
    open_source_info = models.CharField(max_length=100) 
    description = models.TextField() 
    comments = models.TextField()
