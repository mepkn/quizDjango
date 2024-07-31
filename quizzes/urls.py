from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def testfn(request):
    return HttpResponse("quiz app")


urlpatterns = [
    path("test/", testfn),
]
