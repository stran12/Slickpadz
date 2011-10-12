#!/usr/bin/perl
#
# Stephen's script to install all necessary things for Pyramid
# Web Framework



import os



# Things to install
things  =  "git-core \
            build-essential \
            python-setuptools \
            postgreql \
            python-psycopg2 \
            ";

optional_things =  "apache2 \
					"
os.system("sudo apt-get install " + things)

# manually install setup_tools
os.system("sudo python ez_setup.py")

os.system("sudo easy_install virtualenv")
os.system("sudo easy_install sqlalchemy")

# Run the 'virtual --no-site-packages env' command in the /bin directory
# of the env virtualenv dir.


# bin/easy_install pyramid
