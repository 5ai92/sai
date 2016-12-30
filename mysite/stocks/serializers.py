from rest_framework import serializers
from stocks.models import Stocks

class StockSerializer(serializers.Serializer):
	class Meta:
		model = Stocks
		fields = ('id','ticker','name', 'd_open', 'd_close')