from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ctp_website.models import Gig,GigDay,Venue,Composer,Work,Artist,Series

def indextemp(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/indextemp.html',context_dict,context)

def index(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/index.html',context_dict,context)

def test(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/test.html',context_dict,context)


def tickets(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/tickets.html',context_dict,context)


def contact(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/contact.html',context_dict,context)


def support(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/support.html',context_dict,context)

def shost(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}

	context_dict["isShost"] = True
	return render_to_response('ctp_website/shost.html',context_dict,context)


def venues(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}

	v = Venue.objects.order_by('name')
	context_dict['venues'] = v

	return render_to_response('ctp_website/venues.html',context_dict,context)

def all_series(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]
	context_dict = {'GigDay':l}

	s = Series.objects.order_by('name')
	context_dict['series'] = s
	return render_to_response('ctp_website/all_series.html',context_dict,context)

def series(request,series_id):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	try:
		s = Series.objects.get(id=series_id)
		context_dict['series'] = s
		# gigs = s.gig_set.all()
		# context_dict['gigs'] = gigs
	except:
		pass

	return render_to_response('ctp_website/series.html',context_dict,context)



def artist(request,artist_id):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	try:
		a = Artist.objects.get(id=artist_id)
		context_dict['artist'] = a
	except:
		pass

	return render_to_response('ctp_website/artist.html',context_dict,context)

def artists(request):
	context = RequestContext(request)
	a = Artist.objects.order_by('name')
	context_dict = {'artists':a}
	return render_to_response('ctp_website/artists.html',context_dict,context)


def about(request):
	context =  RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/about.html',context_dict,context)

def programme(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di).order_by('time')))]

	context_dict = {'GigDay': l}

	# cott = Venue.objects.get(url = "cottiers")
	# cottl = []
	# for di in d:
	# 	cottl = cottl + [(di,list(Gig.objects.filter(date=di,venue=cott)))]
	# context_dict['cottgigs'] = cottl;

	# hunt = Venue.objects.get(url = "hunterian")
	# huntl = []
	# for di in d:
	# 	huntl = huntl + [(di,list(Gig.objects.filter(date=di,venue=hunt)))]
	# context_dict['huntgigs'] = huntl;

	# silas = Venue.objects.get(url = "stsilas")
	# silasl = []
	# for di in d:
	# 	silasl = silasl + [(di,list(Gig.objects.filter(date=di,venue=silas)))]
	# context_dict['silasgigs'] = silasl;

	return render_to_response('ctp_website/programme.html',context_dict,context)

def day(request,day_url):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}

	try:
		d = GigDay.objects.get(url = day_url)
		g = Gig.objects.filter(date = d).order_by('time')
		context_dict["day"] = d
		context_dict['gigs'] = g
	except:
		pass

	return render_to_response('ctp_website/day.html',context_dict,context)

def dance(request):
	context =  RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	context_dict["isdance"] = True
	return render_to_response('ctp_website/dance.html',context_dict,context)

def gig(request,gig_url):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}

	try:
		g = Gig.objects.get(url = gig_url)
		setattr(g,'hit_count',g.hit_count + 1)
		g.save()
		context_dict['gig'] = g
		print g.hit_count

		musicians = g.artist_set.all().order_by('programme_order')
		context_dict['musicians'] = musicians
		works = g.work_set.all().order_by('programme_order')
		context_dict['works'] = works
		context_dict['about_programme'] = g.about_programme
		context_dict['artist_bio'] = g.artist_bio
		# if 'Bite' in g.title:
		# 	context_dict['subname'] = g.artist_name
		# if 'Currie' in g.title:
		# 	context_dict['subname'] = g.artist_name
		# if 'dance' in g.url:
		# 	context_dict['subname'] = g.artist_name
		# 	context_dict['isdance'] = True
		# if g.price != "empty":
		context_dict['price'] = g.price
	
		# context_dict['bio'] = g.artist_bio
		# if g.musicians != "empty":
		# 	context_dict['musicians'] = g.musicians
		print g.image_url
		if g.image_url!="":
			print g.image_url
			image1 = [g.image_url]
			image1 = image1 + [g.image_width]
			image1 = image1 + [g.image_credit]	
			context_dict['image1'] = image1

		if g.image_url2!="":
			image2 = [g.image_url2]
			image2 = image2 + [g.image_width2]
			image2 = image2 + [g.image_credit2]	
			context_dict['image2'] = image2

		
		# context_dict['programme'] = g.programme
		
		context_dict['about_programme'] = g.about_programme

		
		context_dict['personal_url'] = g.personal_url
		
		context_dict['box_office_url'] = g.box_office_url
	
		context_dict['box_office_url2'] = g.box_office_url2
	
		context_dict['special_offers'] = g.special_offers
	
		context_dict['special_offers2'] = g.special_offers2
	
		context_dict['review_url'] = g.review_url
	
		context_dict['review_url2'] = g.review_url2
	
		context_dict['review_url3'] = g.review_url3



	except:
		pass

	return render_to_response('ctp_website/gig.html',context_dict,context)

def composer(request,composer_id):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	try:
		v = Composer.objects.get(id = composer_id)
		context_dict['composer'] = v
		works = v.work_set.all()
		context_dict['works'] = works
	except:
		pass

	return render_to_response('ctp_website/composer.html',context_dict,context)


def venue(request,venue_id):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	try:
		v = Venue.objects.get(id = venue_id)
		context_dict['venue'] = v
		# if v.contact_number !="empty":
			# context_dict["number"] = v.contact_number
		# if v.image_url != "empty":
		# 	context_dict["image_url"] = v.image_url
		# 	context_dict["image_width"] = v.image_width
		# if v.image_credit != "empty":
		# 	context_dict["image_credit"] = v.image_credit
		# if v.image_url2 != "empty":
		# 	context_dict["image_url2"] = v.image_url2
		# 	context_dict["image_width2"] = v.image_width2
		# if v.image_credit2 != "empty":
		# 	context_dict["image_credit2"] = v.image_credit2


	except:
		pass

	return render_to_response('ctp_website/venue.html',context_dict,context)

def counts(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}

	gigs = Gig.objects.order_by('-hit_count')
	total_count = 0
	for g in gigs:
		total_count += g.hit_count
	context_dict['total_count'] = total_count
	context_dict['gigs'] = gigs

	return render_to_response('ctp_website/counts.html',context_dict,context)	