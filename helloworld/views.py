 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
import os

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        context = {"test": os.environ["DEBUG"]}
        return render(request, 'index.html', context=context)
