# Create your views here.
#

from properties.models import Property, Amenity, Unit
from django.shortcuts import render_to_response

# This next line is IMPORTANT for loading RequestContext into the
# render_to_response so that we can use STATIC_URL global in templates
from django.template import RequestContext 


def index(request):
	return render_to_response('properties/index.html',
						      context_instance=RequestContext(request),
							 )

def search(request):
	properties_list = Property.objects.all()
	return render_to_response('properties/search.html',
							  {'properties_list': properties_list},
						      context_instance=RequestContext(request),
							 )


