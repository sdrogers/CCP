from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ctp_website.models import Gig,GigDay,Venue


def index(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/index.html',context_dict,context)


def tickets(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/tickets.html',context_dict,context)


def contact(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/contact.html',context_dict,context)


def support(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/support.html',context_dict,context)



def venues(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}

	v = Venue.objects.order_by('name')
	context_dict['venues'] = v

	return render_to_response('ctp_website/venues.html',context_dict,context)


def artist(request,artist_name_url):
	context = RequestContext(request)
	context_dict = {'artist_name_url':artist_name_url}
	try:
		a = Artist.objects.get(url__iexact = artist_name_url)
		g = Gig.objects.filter(artist = a)
		context_dict['gigs'] = g
		context_dict['name'] = a.name
		context_dict['genre'] = a.genre
		context_dict['bio'] = a.bio
		if a.image_url != "empty":
			context_dict['image_url'] = a.image_url
			context_dict['image_width'] = a.image_width
			context_dict['image_credit'] = a.image_credit
		if a.image_url2 != "empty":
			context_dict['image_url2'] = a.image_url2
			context_dict['image_width2'] = a.image_width2
			context_dict['image_credit2'] = a.image_credit2
		if a.review_url != "empty":
			context_dict['review_url'] = a.review_url
		if a.review_url2 != "empty":
			context_dict['review_url2'] = a.review_url2
		
		# print a.image
	except:
		pass

	return render_to_response('ctp_website/artist.html',context_dict,context)

def artists(request):
	context = RequestContext(request)
	a = Artist.objects.order_by('name')
	context_dict = {'artists':a}
	return render_to_response('ctp_website/artists.html',context_dict,context)

def genre(request,genre_name):
	context = RequestContext(request)
	context_dict = {'name':genre_name}
	try:
		g = Genre.objects.get(name__iexact = genre_name)
		context_dict['foundname'] = genre_name
		a = Artist.objects.filter(genre = g)
		context_dict['artists'] = a
	except:
		pass

	return render_to_response('ctp_website/genre.html',context_dict,context)

def about(request):
	context =  RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	return render_to_response('ctp_website/about.html',context_dict,context)

def programme(request):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
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

def gig(request,gig_url):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	try:
		g = Gig.objects.get(url = gig_url)
		context_dict['gig'] = g
		if g.artist_bio != "empty":
			context_dict['bio'] = g.artist_bio
		if g.musicians != "empty":
			context_dict['musicians'] = g.musicians
		if g.image_url != "empty":
			image1 = [g.image_url]
			image1 = image1 + [g.image_width]
			if g.image_credit != "empty":
				image1 = image1 + [g.image_credit]	
			context_dict["image1"] = image1
		if g.programme != "empty":
			context_dict["programme"] = g.programme

	except:
		pass

	return render_to_response('ctp_website/gig.html',context_dict,context)


def venue(request,venue_url):
	context = RequestContext(request)
	d = GigDay.objects.order_by('date')
	l = []
	for di in d:
		l = l + [(di,list(Gig.objects.filter(date=di)))]

	context_dict = {'GigDay': l}
	try:
		v = Venue.objects.get(url = venue_url)
		context_dict['venue'] = v
	except:
		pass

	return render_to_response('ctp_website/venue.html',context_dict,context)
