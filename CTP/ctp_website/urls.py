from django.conf.urls import patterns, url
from ctp_website import views

urlpatterns = patterns('',
        url(r'^$', views.indextemp, name='indextemp'),
        url(r'^newindex/$', views.index,name='index'),
        url(r'^artists/',views.artists,name = 'artists'),
        url(r'^about/',views.about,name='about'),
        url(r'^contact/',views.contact,name='contact'),
        url(r'^support/',views.support,name='support'),
        url(r'^venues/',views.venues,name='venues'),
        url(r'^tickets/',views.tickets,name='tickets'),
        url(r'^dance/',views.dance,name="dance"),
        url(r'^programme/',views.programme,name = 'programme'),
        url(r'^day/(?P<day_url>\w+)/$',views.day,name = 'day'),
        url(r'^gig/(?P<gig_url>\w+)/$',views.gig,name = 'gig'),
        url(r'^venue/(?P<venue_id>\w+)/$',views.venue,name = 'venue'),
        url(r'^counts/',views.counts,name='counts'),
        url(r'^shost/',views.shost,name='shost'),
        url(r'^test/',views.test,name='test'),
        url(r'^composer/(?P<composer_id>\w+)/$',views.composer,name='composer'),
        url(r'^artist/(?P<artist_id>\w+)/$',views.artist,name='artist'),
        url(r'^series/(?P<series_id>\w+)/$',views.series,name='series'),
        )