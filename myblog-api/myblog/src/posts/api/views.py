from rest_framework.generics import ListAPIView

from posts.models import *
from .serializers import *

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer