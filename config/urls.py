from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="quizzes/index.html"), name="index"),
    path("questions/", include("quizzes.urls")),
]
