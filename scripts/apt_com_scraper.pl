#!/usr/bin/perl -w
# Script to scrape apartments.com


use strict;




#open(INFILE, "<", "sample_raw.txt");
open(INFILE, "<", "apt_com_LA.txt");

#while (<INFILE>) {
#	if (/<a class="seoURL property-url" ProductId="P" href="(.+)">Check Availability<\/a>/) {
#		print $1, "\n";	
#	}
#
#}
my $url;

for (my $i = 1; $i < 3; $i++) {
	
	$url = "http://www.apartments.com/search/?query=Los%20Angeles,%20CA&stype=CityStateOrZip#searchCriteria=AbAxs6iVO9Lnb1PmYx7yJFnUJvEJNYIEGQVJ9G9aeogmQmeBsKIJ9lJzv8sDB90X6QbYBzDjYy5WZKc/hGowMLntGJE5GyrCgiQIxoAgj9RQavSnjuIbLpY3GHRAFr2ca5dhDu4X0Ql9qWXbcciCuaOv0GzwwZlr6UHaKsjCawU%3D&pagen=$i";

	system("curl -a -o $url sample_raw.txt");

}

close INFILE;

1;

