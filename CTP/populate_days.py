
import os

def populate():
	
	GigDay.objects.all().delete()

	addDay("2014-06-06","Friday")
	addDay("2014-06-07","Saturday")
	addDay("2014-06-08","Sunday")
	addDay("2014-06-09","Monday")
	addDay("2014-06-10","Tuesday")
	addDay("2014-06-11","Wednesday")
	addDay("2014-06-12","Thursday")
	addDay("2014-06-13","Friday")
	addDay("2014-06-14","Saturday")
	addDay("2014-06-15","Sunday")
	addDay("2014-06-16","Monday")
	addDay("2014-06-17","Tuesday")
	addDay("2014-06-18","Wednesday")
	addDay("2014-06-18","Thursday")
	addDay("2014-06-20","Friday")

def addDay(date,day):
	GigDay.objects.get_or_create(date = date,dayOfTheWeek = day)


if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import GigDay
    populate()