from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from posts.models import *
from .serializers import *
from .permissions import *

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsAuthenticated]

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
	#IsOwnerOrReadOnly ensures that the users who is being updated is the owner
	#That is the user who owns the object
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)
