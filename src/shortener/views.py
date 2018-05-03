from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def kirr_FBV(request, *args, **kwargs):
    return HttpResponse("hello")
class Kirr_CBV(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")