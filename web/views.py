from django.shortcuts import render,HttpResponse
from django.http import HttpResponse,JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
# import json


def submit_expense(request):
	# return HttpResponse("Hi Abolfazl")
	print(request.POST)
	return JsonResponse({
		'status':'ok',
	},encoder=DjangoJSONEncoder)