import os

def populate():
	from django.core import serializers
	with open("days.xml",'r') as infile:
		for gigday in serializers.deserialize("xml",infile):
			gigday.save()

	with open("composers.xml","r") as infile:
		for composer in serializers.deserialize("xml",infile):
			composer.save()

	with open("works.xml","r") as infile:
		for work in serializers.deserialize("xml",infile):
			work.save()

	with open("venues.xml","r") as infile:
		for venue in serializers.deserialize("xml",infile):
			venue.save()

	with open("artists.xml","r") as infile:
		for artist in serializers.deserialize("xml",infile):
			artist.save()

	with open("gigs.xml","r") as infile:
		for gig in serializers.deserialize("xml",infile):
			gig.save()


if __name__ == '__main__':
	print "Populating"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
	from ctp_website.models import GigDay, Series, Venue, Composer, Work, Artist, Gig
	populate()