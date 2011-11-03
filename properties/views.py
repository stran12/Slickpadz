# create your views here.
#

from properties.models import Property, Amenity, Unit
from django.shortcuts import render_to_response

# This next line is IMPORTANT for loading RequestContext into the
# render_to_response so that we can use STATIC_URL global in templates
# I think they are called "context processors"
from django.template import RequestContext 
from django.http import Http404

def index(request):
	return render_to_response('properties/index.html',
						      context_instance=RequestContext(request),
							 )
def search(request):
	cityState_or_zip = request.GET.get('cityState_or_zip')
	checklist = [] # This is a checklist of all amenities to be listed in filter panel
	vacancies = [] # Container array to hold all properties with their information for table
	# Main headers outside of amenities checklist.
	# The header of the table will be theaders.extend(checklist)
	theaders  = ['Name', 'Price', 'Bed', 'Bath', 'Type']

	if cityState_or_zip:
		units_list = Unit.objects.select_related().all()
		properties_list = Property.objects.all()

		# This loop is to grab all possible amenities for properties we are
		# going to list
		for p in properties_list:
			 amenities = p.amenities.all()
			 # Append all unique amenities into checklist
			 for amenity in amenities:
				 if checklist.count(amenity.name) == 0:
			 	 	checklist.append(amenity.name)


		# Loop through properties again and make a 
		for u in units_list:
			attr = {}
			attr['name'] 	    = u.prop.name
			attr['bed'] 	    = u.bed
			attr['bath'] 	    = u.bath
			attr['price_low']   = u.price_low
			attr['price_high']  = u.price_high
			attr['address'] 	= u.prop.address
			attr['city'] 		= u.prop.city.name
			attr['state'] 		= u.prop.state.name
			attr['zip_code'] 	= u.prop.zip_code
			attr['manager'] 	= u.prop.manager.name
			attr['phone'] 		= u.prop.phone
			attr['prop_url'] 	= u.prop.prop_url
			attr['prop_type'] 	= u.prop.prop_type.name

			prop_amen_list = []

			for amenity in checklist:
				try:
					does_exist = u.prop.amenities.get(name=amenity)
				except Amenity.DoesNotExist:
					prop_amen_list.append('')
				else:
					prop_amen_list.append(does_exist)
		
			attr['amenities_list'] = prop_amen_list
			
			vacancies.append(attr)
					

		return render_to_response('properties/search.html',
				{'checklist': checklist,
				 'vacancies': vacancies,
				 'theaders' : theaders,
				}
				,context_instance=RequestContext(request),
				)
	# Otherwise, if there is no cityState_or_zip
	else:
		raise Http404

def properties(request):
	from django.http import HttpResponse
	return HttpResponse("HELLO WORLD")

