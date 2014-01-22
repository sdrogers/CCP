from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ctp_website.models import Artist,Gig,GigDay


def index(request):
	context = RequestContext(request)
	context_dict = {'hello':"hello"}
	return render_to_response('ctp_website/index.html',context_dict,context)

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
	return render_to_response('ctp_website/about.html')

def programme(request):
	context = RequestContext(request)
	g = GigDay.objects.order_by('date')
	print g
	context_dict = {'gigDays':g}	
	these = Gig.objects.filter(date = g[0])
	context_dict['test'] = these
	print these
	return render_to_response('ctp_website/programme.html',context_dict,context)