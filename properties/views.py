# Create your views here.
#

from properties.models import Property, Amenity, Unit
from django.shortcuts import render_to_response

def index(request):
	properties_list = Property.objects.all()
	return render_to_response('properties/index.html', {'properties_list': properties_list})



