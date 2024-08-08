from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from quizzes import views

urlpatterns = [
    path("new/", view=views.new_game, name="new"),
    path("complete/", view=views.complete, name="complete"),
    path("question/", view=views.next_question, name="question"),
    path("question/<int:pk>/", view=views.question_view, name="question"),
    path(
        "question/<int:question_pk>/choice/<int:choice_pk>",
        view=views.answer_view,
        name="answer",
    ),
]
