#!/usr/bin/python

from bs4 import BeautifulSoup
from urllib2 import urlopen

# URL of Computer Market venue website
# TODO: don't hardcode URL; build URL parameters and allow for other locations
URL = "http://www.computermarkets.com/cm/index.php?view=venueevents&id=18:newcastle-pcyc%20Broadmeadow"

def fetch_dates(url):
	""" Fetches dates of upcoming computer market dates for a given `computermarkets.com` URL. """
	
	html = urlopen(URL).read()
	soup = BeautifulSoup(html, "lxml")
	
	for date in soup.findAll("td", attrs={ "headers" : "el_date" }):
		print date.get_text(strip=True)
		
if __name__ == '__main__':
	fetch_dates(URL)
	