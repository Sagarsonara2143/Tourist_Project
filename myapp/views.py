from django.shortcuts import render
from .models import User
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


def register(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Id is already registered"
			return render(request,'register.html',{'msg':msg,'is_register_page':True})
		except:
			try:
				User.objects.get(mobile=request.POST['mobile'])	
				msg="Mobile Number Already Registred"
				return render(request,'register.html',{'msg':msg,'is_register_page':True})
			except:
				if request.POST['password']==request.POST['confirm_password']:
					User.objects.create(
						first_name=request.POST['first_name'],
						last_name=request.POST['last_name'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_picture=request.FILES['profile_pic'],
						)
					msg="User Sign Up Successfully"
					return render(request,'login.html',{'msg':msg,'is_register_page':True})
				else:
					msg="Password and Confirm password does not matched"
					return render(request,'register.html',{'msg':msg,'is_register_page':True})
	else:
		return render(request,"register.html",{'is_register_page':True})
