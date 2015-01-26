from django.db import models

# class Genre(models.Model):
# 	name = models.CharField(max_length = 124, unique = True)
# 	def __unicode__(self):
# 		return self.name



class Venue(models.Model):
	name = models.CharField(max_length = 1024,unique=True)
	address = models.CharField(max_length = 1024,unique =True)
	contact_number = models.CharField(max_length = 20,null = True)
	image_url = models.CharField(max_length = 1024,default = "empty")
	image_url2 = models.CharField(max_length = 1024,default = "empty")
	image_url3 = models.CharField(max_length = 1024,default = "empty")
	image_width = models.IntegerField(default = "400")
	image_width2 = models.IntegerField(default = "200")
	image_width3 = models.IntegerField(default = "100")
	image_credit = models.CharField(max_length = 1024,default = "empty")
	image_credit2 = models.CharField(max_length = 1024,default = "empty")
	image_credit3 = models.CharField(max_length = 1024,default = "empty")
	info = models.CharField(max_length = 10240,default = "empty")
	url = models.CharField(max_length = 1024,null = True)
	def __unicode__(self):
		return self.name


class GigDay(models.Model):
	date = models.DateField()
	dayOfTheWeek = models.CharField(max_length = 32,default = "empty")
	url = models.CharField(max_length = 1024)
	img_url = models.CharField(max_length = 1024,default = "empty")
	def __unicode__(self):
		return self.dayOfTheWeek

class Gig(models.Model):
	title = models.CharField(max_length=1024)
	artist_name = models.CharField(max_length=1024)
	artist_bio = models.CharField(max_length=10240,default = "empty")
	date = models.ForeignKey(GigDay)
	time = models.TimeField()
	venue = models.ForeignKey(Venue,null=True)
	url = models.CharField(max_length=1024)
	programme = models.CharField(max_length = 10240,default = "empty")
	about_programme = models.CharField(max_length = 10240,default = "empty")
	musicians = models.CharField(max_length = 1024,default = "empty")
	personal_url = models.CharField(max_length = 1024,default = "empty")
	review_url = models.CharField(max_length = 1024,default = "empty")
	review_url2 = models.CharField(max_length = 1024,default = "empty")
	review_url3 = models.CharField(max_length = 1024,default = "empty")
	blog_url = models.CharField(max_length = 1024,default = "empty")
	price = models.CharField(max_length = 1024,default = "empty")
	box_office_url = models.CharField(max_length = 1024,default = "empty")
	box_office_url2 = models.CharField(max_length = 1024,default = "empty")
	special_offers = models.CharField(max_length = 1024,default = "empty")
	special_offers2 = models.CharField(max_length = 1024,default = "empty")
	emergency_field = models.CharField(max_length = 10240,default = "empty")
	image_url = models.CharField(max_length = 1024,default = "empty")
	image_url2 = models.CharField(max_length = 1024,default = "empty")
	image_width = models.IntegerField(default = "400")
	image_width2 = models.IntegerField(default = "200")
	image_credit = models.CharField(max_length = 1024,default = "empty")
	image_credit2 = models.CharField(max_length = 1024,default = "empty")

	spare = models.CharField(max_length = 10240, default = "empty")
	hit_count = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.title

class Musician(models.Model):
	name = models.CharField(max_length=256)
	instrument = models.CharField(max_length=256)
	gigs = models.ManyToManyField(Gig)

	def __unicode__(self):
		return self.name

	



