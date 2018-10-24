 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        context = {"test": "OK!"}
        return render(request, 'index.html', context=context)
