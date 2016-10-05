from rest_framework.serializers import ModelSerializer

from posts.models import *

class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'content']