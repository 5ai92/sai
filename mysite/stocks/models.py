from django.db import models


# Create your models here.

class Stocks(models.Model):
	symbol = models.CharField(max_length =20)
	company = models.CharField(max_length = 100)

	def __unicode__(self):
		return "%s %s" %(self.symbol, self.company)


	def __str__(self):
		return "%s %s" %(self.symbol, self.company)

	



