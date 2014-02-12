from django.db import models

from model_utils import Choices

class Software(models.Model):

    LICENSE_MODELS = Choices(
        ('open_source', 'Open Source'),
        ('freeware', 'Freeware'),
        ('academic', 'Free for academics'),
        ('shareware', 'Shareware'),
        ('commercial', 'Commercial'),
        )

    name = models.CharField(max_length=50)
    url = models.URLField()
    categories = models.CharField(max_length=80)
    other_categories = models.CharField(max_length=50)
    license_model = models.CharField(choices=LICENSE_MODELS, max_length=40)
    open_source_info = models.CharField(max_length=100) 
    description = models.TextField() 
    comments = models.TextField()

    def __unicode__(self):
        return self.name
