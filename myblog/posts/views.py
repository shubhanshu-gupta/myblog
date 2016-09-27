from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def fetch_post(request):
	return HttpResponse("yo")

def create_post(request, id):
	instance = get_object_or_404(Post, id=id)
	# post_id = request.GET.get('id', None)
	# return HttpResponse(instance)
	context = {
		"queryset": instance,
		"title": "Shubhanshu Gupta"
	}
	return render(request, "index.html", context)

def detail_post(request, id=None):
	queryset_list = Post.objects.all()#.order_by('-timestamp')
	paginator = Paginator(queryset_list, 2)
	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

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

def update_post(request, id=None):
	instance = get_object_or_404(Post, id=id)

	if not request.user.is_authenticated():
		raise Http404

	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		# print form.cleaned_data.get("title")
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, "Not updated")
# 	if request.method == 'POST':
# #		print request.POST
# 		print request.POST.get('title')
# 		print request.POST.get('content')
	context = {
		"title": instance.title,
		"content": instance.content,
		"form": form,
	}
	return render(request, "post_form.html", context)

def delete_post(request):
	return HttpResponse("yo4")

