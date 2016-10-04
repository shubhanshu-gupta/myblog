from rest_framework.generics import ListAPIView

from posts.models import *

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()