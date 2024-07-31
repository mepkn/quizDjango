from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def testfn(request):
    return HttpResponse("Testing 1 2 3 ... OK")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", testfn),
    path("quiz/", include("quizzes.urls")),
]
