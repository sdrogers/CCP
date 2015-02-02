import os

def dump():
	from django.core import serializers
	v = Venue.objects.all()
	for venue in v:
		print venue.name
	with open("venus.xml", "w") as out:
		serializers.serialize("xml",Venue.objects.all(),stream=out)

	with open("series.xml","w") as out:
		serializers.serialize("xml",Series.objects.all(),stream=out)		



if __name__ == '__main__':
    print "Starting dump script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import Venue,Series
    dump()