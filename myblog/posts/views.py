from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
#The view handles the request in return of the response


def fetch_post(request):
	return HttpResponse("yo")

def create_post(request, id):
	instance = get_object_or_404(Post, id=id)
	# post_id = request.GET.get('id', None)
	return HttpResponse(instance)

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
	form = PostForm()
	if request.method == 'POST':
#		print request.POST
		print request.POST.get('title')
		print request.POST.get('content')
	context = {
		"form": form
	}
	return render(request, "post_form.html", context)

def delete_post(request):
	return HttpResponse("yo4")

