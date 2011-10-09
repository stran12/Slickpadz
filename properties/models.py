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
	
class Unit(models.Model):
	number 	= models.CharField(max_length=10)
	bed     = models.IntegerField()
	bath	= models.IntegerField()



class Amenity(models.Model):
	prop = models.ManyToManyField(Property)
	name = models.CharField(max_length=50)
	pet_choices = (
		('c','Cats'),
		('d','Dogs'),
		('b','Both'),
		('n','None'),
	)
	pets = models.CharField(max_length=1, choices = pet_choices)


