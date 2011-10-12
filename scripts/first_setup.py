#!/usr/bin/perl
#
# Stephen's script to install all necessary things for Pyramid
# Web Framework



import os



# Things to install
things  =  "git-core \
            build-essential \
            python-setuptools \
			python-psycopg2 \
			postgresql-8.4 \
            ";

optional_things =  "apache2"



print "Unzipping Django-1.3.1.tar.gz\n"
os.system("tar xzvf Django-1.3.1.tar.gz")

print "cd Django-1.3.1\n"
os.system("cd Django-1.3.1")

print "Installing Django-1.3.1...\n"
os.system("sudo python setup.py install")

print "Going back up to /home/user\n"
os.sytem("cd ..")

print "Going to INSTALL a lot of stuff now\n"
os.system("sudo apt-get install " + things)

#os.system("git config --global user.name \"Stephen Tran\"")
#os.system("git config --global user.email dreamer7321@yahoo.com")
#os.system("git config --global color.ui true")



