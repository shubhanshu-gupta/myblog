from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "at_created"]
	list_filter = ["updated", "at_created"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)