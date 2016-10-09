from rest_framework.serializers import ModelSerializer

from posts.models import *

class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['user', 'title', 'slug', 'content', 'publish']


""""
from posts.models import Post
from posts.api.serializers import PostSerializer
data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",

}
obj = Post.objects.get(id=2)

##Below method is used to update the object of Post model with the data
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""