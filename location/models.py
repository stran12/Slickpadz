from django.db import models

# Create your models here.


class State(models.Model):
	name = models.CharField(max_length=15)
	abbrev = models.CharField(max_length=2)
	def __unicode__(self):
		return self.name


class City(models.Model):
	state = models.ForeignKey(State)
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.name
