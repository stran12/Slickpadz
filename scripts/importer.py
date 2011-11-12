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
from location.models import *

import math
import requests
import re
import json


# property_id
# property_nm
# url_nm
# type_nm
# contact


ph = PhoneNumber.objects.create(
        number="3105551234"
        )
city  = City.objects.get(name='Los Angeles')
state = State.objects.get(name='California')
lt    = LeaseType.objects.create(
                name = "1 year",
                )
st    = Status.objects.create(
                name = "active",
                )

i = 0
with open("rent_com_sample.txt") as f:
    for line in f:
        if i == 10:
            break
        else:
            i = i+1
        (purl, pname, psite, ptype, pmanager, paddress, pcity, pstate, ubed, ubath, umin, umax, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19) = line.split("\t")
#        print pname
        man = Manager.objects.create(
                name        = pmanager,
                phone       = ph,
                url         = psite
                )


        s = Source.objects.create(
                name        = pmanager,
                url         = "www.rent.com"
                )

        pt = PropertyType.objects.create(
                name        = ptype
                )

        p = 0;
        try:
            p = Property.objects.get(address=paddress)
        except Property.DoesNotExist:
            p = Property.objects.create(
                name        = pname,
                address     = paddress,
                city        = city,
                state       = state,
                zip_code    = 90064,
                manager     = man,
                source      = s,
                prop_url    = "http://rent.com/" + purl,
                prop_type   = pt,
                lease_type  = lt,
                status      = st
                )
            p.phone.add(ph)

        Unit.objects.create(
                prop        = p,
                number      = "A",
                bed         = int(ubed),
                bath        = int(float(ubath)) if ubath != '' else 0,
                price_low   = int(umax) if (umin == '') else int(umin),
                price_high  = int(umax)
                )





print "Done\n"






