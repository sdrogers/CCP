
import os

def populate():
	
	GigDay.objects.all().delete()

	addDay("2014-06-06","Friday","jun6")
	addDay("2014-06-07","Saturday","jun7")
	addDay("2014-06-08","Sunday","jun8")
	addDay("2014-06-09","Monday","jun9")
	addDay("2014-06-10","Tuesday","jun10")
	addDay("2014-06-11","Wednesday","jun11")
	addDay("2014-06-12","Thursday","jun12")
	addDay("2014-06-13","Friday","jun13")
	addDay("2014-06-14","Saturday","jun14")
	addDay("2014-06-15","Sunday","jun15")
	addDay("2014-06-16","Monday","jun16")
	addDay("2014-06-17","Tuesday","jun17")
	addDay("2014-06-18","Wednesday","jun18")
	addDay("2014-06-19","Thursday","jun19")
	addDay("2014-06-20","Friday","jun20")

def addDay(date,day,url):
	GigDay.objects.get_or_create(date = date,dayOfTheWeek = day,url = url)


if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import GigDay
    populate()