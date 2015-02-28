import os

def dump():
	from django.core import serializers
	with open("days.xml", "w") as out:
		serializers.serialize("xml",GigDay.objects.all(),stream=out)

	with open("series.xml","w") as out:
		serializers.serialize("xml",Series.objects.all(),stream=out)		

	with open("venues.xml","w") as out:
		serializers.serialize("xml",Venue.objects.all(),stream=out)		

	with open("composers.xml","w") as out:
		serializers.serialize("xml",Composer.objects.all(),stream=out)

	with open("works.xml","w") as out:
		serializers.serialize("xml",Work.objects.all(),stream=out)

	with open("artists.xml","w") as out:
		serializers.serialize("xml",Artist.objects.all(),stream=out)

	with open("gigs.xml","w") as out:
		serializers.serialize("xml",Gig.objects.all(),stream=out)	

if __name__ == '__main__':
    print "Starting day dump script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import GigDay, Series, Venue, Composer, Work, Artist, Gig
    dump()