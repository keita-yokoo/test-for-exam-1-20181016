# helloworld/urls.py
from django.conf.urls import url
from exam.views.index import index

urlpatterns = [
    url(r'^$', index.HomePageView.as_view()),
]
