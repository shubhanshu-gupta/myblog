from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	at_created = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return "%s" % self.title