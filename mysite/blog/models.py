from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField(max_length =10000)
	date = models.DateTimeField()



	def __str__ (self):
		return self.title
