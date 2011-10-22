from django.db import models
from location.models import State, City
# Create your models here.

import datetime

class PhoneNumber(models.Model):
	number = models.CharField(max_length=10)
	ext    = models.CharField(max_length=6)
	def __unicode__(self):
		return self.number + ' ' + self.ext

class Source(models.Model):
	name = models.CharField(max_length=50)
	url  = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name


class Manager(models.Model):
	name	= models.CharField(max_length=50)
	phone	= models.ForeignKey(PhoneNumber)
	url		= models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class PropertyType(models.Model):
	name = models.CharField(max_length=15)
	def __unicode__(self):
		return self.name


class Property(models.Model):
	name	 	= models.CharField(max_length=50)
	address	  	= models.CharField(max_length=50)
	city 		= models.ForeignKey(City)
	state		= models.ForeignKey(State)
	zip_code	= models.IntegerField()
	manager     = models.ForeignKey(Manager)
	phone		= models.OneToOneField(PhoneNumber)
	source		= models.ForeignKey(Source)
	prop_url	= models.CharField(max_length=200)
	prop_type	= models.ForeignKey(PropertyType)
	latitude  	= models.FloatField()
	longitude  	= models.FloatField()
	def __unicode__(self):
		return self.name
	
class Unit(models.Model):
	prop    = models.ForeignKey(Property)
	number 	= models.CharField(max_length=10)
	bed     = models.IntegerField()
	bath	= models.IntegerField()
	sqft	= models.IntegerField()
	price_low = models.IntegerField()
	price_high= models.IntegerField()
	deposit = models.IntegerField()
	def __unicode__(self):
		return self.number

class Amenity(models.Model):
	prop = models.ManyToManyField(Property)
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name


















