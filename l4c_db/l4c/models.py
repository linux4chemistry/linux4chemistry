import uuid

from django.db import models


class _SoftwareCategory(models.Model):

    label = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class LicenseModel(_SoftwareCategory):
    pass


class Category(_SoftwareCategory):
    pass


class Software(models.Model):

    id = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=50)
    url = models.URLField()
    categories = models.ManyToManyField(Category)
    other_categories = models.CharField(max_length=50)
    license_model = models.ForeignKey(LicenseModel)
    open_source_info = models.CharField(max_length=100) 
    description = models.TextField() 
    comments = models.TextField()

    def all_categories(self):
        """Return the associated categories and those listed as 'other_categories'"""
        categories = list(c.name for c in self.categories.all())
        if self.other_categories:
            categories += map(lambda c: c.strip(), self.other_categories.split(','))
        return ', '.join(categories)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4())
        super(Software, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
