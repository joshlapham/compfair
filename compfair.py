#!/usr/bin/python

###
#
# compfair.py
# Scrapes the ComputerMarkets.com website for upcoming dates in my local area.
#
# By Josh Lapham [josh@joshlapham.com]
#
# https://github.com/joshlapham/compfair
#
# License: Beerware
# 
###

from bs4 import BeautifulSoup
from urllib2 import urlopen

# URL of Computer Market venue website
url = "http://www.computermarkets.com/cm/index.php?view=venueevents&id=18:newcastle-pcyc%20Broadmeadow"
# Beautiful Soup variables
html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

# Loop over the <td> elements for the 'el_date' headers
for date in soup.findAll("td", attrs={ 'headers' : "el_date" }):
	# Print only the dates in the tags and strip any whitespace
	print date.get_text(strip=True)