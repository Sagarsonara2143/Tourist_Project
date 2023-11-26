from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,"index.html",{'is_home_page': True})


def about(request):
	return render(request,"about.html",{'is_about_page': True})
