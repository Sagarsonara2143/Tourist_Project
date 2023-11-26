from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,"index.html",{'is_home_page': True})


def about(request):
	return render(request,"about.html",{'is_about_page': True})

def service(request):
	return render(request,"service.html",{'is_service_page':True})

def package(request):
	return render(request,"package.html",{'is_package_page':True})

def destination(request):
	return render(request,"destination.html",{'is_destination_page':True})


def booking(request):
	return render(request,"booking.html",{'is_booking_page':True})


def team(request):
	return render(request,"team.html",{'is_team_page':True})

def testimonial(request):
	return render(request,"testimonial.html",{'is_testimonial_page':True})

def contact(request):
	return render(request,"contact.html",{'is_contact_page':True})