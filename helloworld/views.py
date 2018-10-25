 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
import os
from django.conf import settings

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            "test": settings.DEBUG,
            "a": settings.A_TEST,
            "b": settings.TEST
        }
        return render(request, 'index.html', context=context)
