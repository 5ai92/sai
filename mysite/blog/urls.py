from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views



urlpatterns = [

	url(r'^blog$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name = "blog/blog.html")),
	url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name ='blog/post.html')),
	
]