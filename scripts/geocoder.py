# Geocoder.py -- stephen tran 
#
# This script will pull all addresses of properties from the database that does
# not have a latitude of longitude and hit Google's geocode api to fill that in.
# Currently (11/2/2011), Google capped requests to 2,500/day. This will
# eventually turn into a cron job.
#
# After appending these directories to the PYTHONPATH, we are then able to use
# the statement: "from properties.models import *"
import sys
sys.path.append('/home/stephen')
sys.path.append('/home/stephen/slickpadz')

from django.conf import settings
from django.db import models

from properties.models import *
import requests
import re
import json



properties = Property.objects.select_related('city', 'state').all()

for p in properties:
    url = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=' \
            + p.address +' '+ p.city.name +', '+ p.state.name

    url = re.sub(r'\s', r'+',url)

    print url
    r = requests.get(url)

    print "STATUS ",  r.status_code, "\n"
    #print r.content
    j = json.loads(r.content)
    #print j["results"][0]["geometry"]["location"]
    p.latitude = j["results"][0]["geometry"]["location"]["lat"]
    p.longitude = j["results"][0]["geometry"]["location"]["lng"]
    p.save()
 


