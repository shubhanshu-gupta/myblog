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

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
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
	filter_backends = [SearchFilter, OrderingFilter]
	pagination_class = LimitOffsetPagination #PageNumberPagination

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	#IsOwnerOrReadOnly ensures that the users who is being updated is the owner
	#That is the user who owns the object
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)
