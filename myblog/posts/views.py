from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#The view handles the request in return of the response


def fetch_post(request):
	return HttpResponse("yo")


def create_post(request):
	return HttpResponse("yo1")

def detail_post(request):
	return HttpResponse("yo2")

def update_post(request):
	return HttpResponse("yo3")

def delete_post(request):
	return HttpResponse("yo4")

