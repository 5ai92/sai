from django.shortcuts import render

# Create your views here.


def form(request):
	return(request, 'blog/postform.html')