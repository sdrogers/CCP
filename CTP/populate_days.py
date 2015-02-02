
import os

def populate():
	
	GigDay.objects.all().delete()

	addDay("2014-06-05","Friday","jun5")
	addDay("2014-06-06","Saturday","jun6")
	addDay("2014-06-07","Sunday","jun7")
	addDay("2014-06-08","Monday","jun8")
	addDay("2014-06-19","Tuesday","jun9")
	addDay("2014-06-10","Wednesday","jun10")
	addDay("2014-06-11","Thursday","jun11")
	addDay("2014-06-12","Friday","jun12")
	addDay("2014-06-13","Saturday","jun13")
	addDay("2014-06-14","Sunday","jun14")
	addDay("2014-06-15","Monday","jun15")
	addDay("2014-06-16","Tuesday","jun16")
	addDay("2014-06-17","Wednesday","jun17")
	addDay("2014-06-18","Thursday","jun18")
	addDay("2014-06-19","Saturday","jun19")
	addDay("2014-06-20","Sunday","jun20")
	addDay("2014-06-21","Monday","jun21")
	addDay("2014-06-22","Tuesday","jun22")
	addDay("2014-06-23","Wednesday","jun23")
	addDay("2014-06-24","Thursday","jun24")
	addDay("2014-06-25","Friday","jun25")
	addDay("2014-06-26","Saturday","jun26")


def addDay(date,day,url):
	GigDay.objects.get_or_create(date = date,dayOfTheWeek = day,url = url)

def populate_venues():
	from django.core import serializers
	from ctp_website.models import Venue
	with open('venus.xml') as data:
		for obj in serializers.deserialize("xml", data):
			obj.save()

if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import GigDay
    populate()
    populate_venues()