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