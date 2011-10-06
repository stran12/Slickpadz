from django.db import models
from location.models import State, City
# Create your models here.

import datetime


class Property(models.Model):
	city = models.ForeignKey(City)
	latitude  = models.IntegerField()
	longitude = models.IntegerField()
	address	  = models.CharField(max_length=50)
	

class Unit(models.Model):
	number 	= models.CharField(max_length=10)
	bed		= models.IntegerField()
	bath	= models.IntegerField()

class Amenity(models.Model):
	unit = ForeignKey(Unit)
	pet_choices = (
		('c','Cats'),
		('d','Dogs'),
		('b','Both'),
		('n','None'),
	)
	pets = models.CharField(max_length=1, choices = pet_choices)
	hardwood_floors 	= models.BooleanField()
	air_conditioning	= models.BooleanField()
	fitness_center 		= models.BooleanField()
	laundry_room		= models.BooleanField()
	garage_parking		= models.BooleanField()
	pool				= models.BooleanField()
	washerdryer_inunit  = models.BooleanField()
	washerdryer_hookup  = models.BooleanField()
	walkin_closet		= mdoels.BooleanField()

	




