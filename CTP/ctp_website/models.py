from django.db import models

# class Genre(models.Model):
# 	name = models.CharField(max_length = 124, unique = True)
# 	def __unicode__(self):
# 		return self.name



class Venue(models.Model):
	name = models.CharField(max_length = 1024,unique=True)
	address = models.CharField(max_length = 1024,unique =True)
	contact_number = models.CharField(max_length = 20,null = True,blank=True)
	image_url = models.CharField(max_length = 1024,null=True,blank=True)
	image_url2 = models.CharField(max_length = 1024,blank=True,null=True)
	image_url3 = models.CharField(max_length = 1024,blank=True,null=True)
	image_width = models.IntegerField(default = "400")
	image_width2 = models.IntegerField(default = "200")
	image_width3 = models.IntegerField(default = "100")
	image_credit = models.CharField(max_length = 1024,blank=True,null=True)
	image_credit2 = models.CharField(max_length = 1024,blank=True,null=True)
	image_credit3 = models.CharField(max_length = 1024,blank=True,null=True)
	info = models.CharField(max_length = 10240,blank=True,null=True)
	url = models.CharField(max_length = 1024,null = True)
	nearest_subway = models.CharField(max_length=124,null=True,blank=True)
	nearest_bus = models.CharField(max_length=124,null=True,blank=True)
	google_maps = models.CharField(max_length=1024,null=True,blank=True)
	def __unicode__(self):
		return self.name

class Series(models.Model):
	name = models.CharField(max_length=256,null=True,blank=True)
	bio = models.CharField(max_length=10240,null=True,blank=True)
	url = models.CharField(max_length=32,null=True,blank=True)
	image_url = models.CharField(max_length = 1024,null=True,blank=True)
	image_width = models.IntegerField(default="400",null=True,blank=True)
	image_credit = models.CharField(max_length="1024",null=True,blank=True)
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
	# artist_name = models.CharField(max_length=1024,null=True)
	# artist_bio = models.CharField(max_length=10240,default = "empty")
	series = models.ForeignKey(Series,null=True,blank=True)
	date = models.ForeignKey(GigDay)
	time = models.TimeField()
	venue = models.ForeignKey(Venue,null=True)
	url = models.CharField(max_length=1024)
	# programme = models.CharField(max_length = 10240,null=True,blank=True)
	about_programme = models.CharField(max_length = 10240,null=True,blank=True)
	# musicians = models.CharField(max_length = 1024,null=True,blank=True)
	personal_url = models.CharField(max_length = 1024,null=True,blank=True)
	review_url = models.CharField(max_length = 1024,null=True,blank=True)
	review_url2 = models.CharField(max_length = 1024,null=True,blank=True)
	review_url3 = models.CharField(max_length = 1024,null=True,blank=True)
	blog_url = models.CharField(max_length = 1024,null=True,blank=True)
	price = models.CharField(max_length = 1024,null=True,blank=True)
	box_office_url = models.CharField(max_length = 1024,null=True,blank=True)
	box_office_url2 = models.CharField(max_length = 1024,null=True,blank=True)
	special_offers = models.CharField(max_length = 1024,null=True,blank=True)
	special_offers2 = models.CharField(max_length = 1024,null=True,blank=True)
	emergency_field = models.CharField(max_length = 10240,null=True,blank=True)
	image_url = models.CharField(max_length = 1024,null=True,blank=True)
	image_url2 = models.CharField(max_length = 1024,null=True,blank=True)
	image_width = models.IntegerField(default = "400")
	image_width2 = models.IntegerField(default = "200")
	image_credit = models.CharField(max_length = 1024,null=True,blank=True)
	image_credit2 = models.CharField(max_length = 1024,null=True,blank=True)

	spare = models.CharField(max_length = 10240, null=True,blank=True)
	hit_count = models.IntegerField(default = 0)

	

	def __unicode__(self):
		return self.title



class Artist(models.Model):
	name = models.CharField(max_length=256)
	instrument = models.CharField(max_length=256,null=True,blank=True)
	bio = models.CharField(max_length=1024,null=True,blank=True)
	gigs = models.ManyToManyField(Gig,blank=True)

	def __unicode__(self):
		return self.name

class Composer(models.Model):
	name = models.CharField(max_length=256)
	bio = models.CharField(max_length=1024,null=True,blank=True)
	
	def __unicode__(self):
		return self.name

class Work(models.Model):
	name = models.CharField(max_length=256)
	bio = models.CharField(max_length=1024,null=True,blank=True)
	composer = models.ForeignKey(Composer)
	gigs = models.ManyToManyField(Gig)

	def __unicode__(self):
		return self.name




