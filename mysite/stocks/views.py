from django.shortcuts import render
from django.http import HttpResponse
from stocks.models import Stocks


# Create your views here.


def stockslist(request):
	symbols = [x.encode('UTF8') for x in Stocks.objects.values_list('symbol', flat = True)]
	companies = [x.encode('UTF8') for x in Stocks.objects.values_list('company', flat = True)]
	context = {
	"symbol": symbols,
	"company": companies
	}
	return render(request,'stocks/stocklist.html',context)


#def stocksdetail(request):
#	return render(request, 'stocks/stocksdetail.html',context)
