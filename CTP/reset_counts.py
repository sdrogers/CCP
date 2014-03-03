import os

def reset_counts():
	gigs = Gig.objects.all();
	for g in gigs:
		a = g.hit_count
		setattr(g,'hit_count',0)
		g.save()
		print a,g.hit_count


if __name__ == '__main__':
    print "Resetting counts..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CTP.settings')
    from ctp_website.models import Gig
    reset_counts()