from django.urls import path, include

urlpatterns = [
    path(
        "hostutils/",
        include("djangoaddicts.hostutils.urls"),
    ),
]
