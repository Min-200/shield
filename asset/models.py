from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models

# Create your models here.


class Asset(models.Model):
	created_time = models.DateTimeField(default=timezone.now)
	asset_name = models.CharField(max_length=10)
	asset_number = models.CharField(max_length=20)
	asset_source = models.CharField(max_length=10)
	asset_people = models.CharField(max_length=100)
	asset_application = models.CharField(max_length=100)
	
	def __unicode__(self):
                return "%s,%s,%s,%s,%s,%s"%(self.created_time, self.asset_name, self.asset_number, self.asset_source, self.asset_people, self.asset_application)
