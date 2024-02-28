from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path(
        "hostutils/",
        include("djangoaddicts.hostutils.urls"),
    ),
    path('', lambda request: HttpResponse('hello world', content_type='text/plain'), name="home"),

]
