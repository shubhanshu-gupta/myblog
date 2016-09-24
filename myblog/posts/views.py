from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.
#The view handles the request in return of the response


def fetch_post(request):
	return HttpResponse("yo")


def create_post(request):
	return HttpResponse("yo1")

def detail_post(request):
	queryset = Post.objects.all()
	context = {
		"queryset": queryset,
		"title": "Shubhanshu Gupta"
	}
	# if request.user.is_authenticated:
	# 	context = {
	# 		"title": "Shubhanshu Gupta"
	# 	}
	# else:
	# 	context = {
	# 		"title": "Somebody"
	# 	}

	return render(request, "index.html", context)

def update_post(request):
	return HttpResponse("yo3")

def delete_post(request):
	return HttpResponse("yo4")

