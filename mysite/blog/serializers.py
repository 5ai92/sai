from django.db import models


class PostSerializer(serializers.Serializer):
	
	title = serializer.CharField(max_length =50)
	body = serializer.TextField(max_lenth =10000)
	date = serializer.DateField()


