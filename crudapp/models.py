from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return ' '. join([ self.first_name, self.last_name, ])

