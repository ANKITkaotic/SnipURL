from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from shortener.models import KirrURL

def kirr_FBV(request,shortcode = None, *args, **kwargs):
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

    
class Kirr_CBV(View):
    def get(self, request, shortcode = None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode = shortcode)
        return HttpResponseRedirect(obj.url)