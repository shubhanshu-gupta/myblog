from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView
	)

from posts.models import *
from .serializers import *

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)
