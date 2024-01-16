# from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .task import test_func, test_func1
# Create your views here.
def test(request):
    test_func.delay()
    test_func1.delay()
    return HttpResponse("Done with test request")