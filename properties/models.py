from django.db import models
from location.models import State, City
# Create your models here.

import datetime


class Property(models.Model):
	city = models.ForeignKey(City)
	name = models.CharField(max_length=50)
	latitude  = models.IntegerField()
	longitude = models.IntegerField()
	address	  = models.CharField(max_length=50)
	price     = models.IntegerField()
	def __unicode__(self):
		return self.name

	
class Unit(models.Model):
	number 	= models.CharField(max_length=10)
	bed     = models.IntegerField()
	bath	= models.IntegerField()
	def __unicode__(self):
		return self.number

class Amenity(models.Model):
	prop = models.ManyToManyField(Property)
	name = models.CharField(max_length=50)
	pet_choices = (
		('c','Cats'),
		('d','Dogs'),
		('b','Both'),
		('n','None'),
	)
	#pets = models.CharField(max_length=1, choices = pet_choices)
	def __unicode__(self):
		return self.name

class PhoneNumber(models.Model):
	number = models.CharField(max_length=10)
	ext    = models.CharField(max_length=6)
	def __unicode__(self):
		return self.number + ' ' + self.ext



class Sources(models.Model):
	name = models.CharField(max_length=50)
	url  = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name



