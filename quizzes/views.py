from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Question


# Display questions and choices
def question_view(request, pk):
    q = get_object_or_404(Question, pk=pk)
    context = {"question": q}
    return render(request, "quizzes/question.html", context=context)


# Check if answer is correct
def answer_view(request, question_pk, choice_pk):
    q = get_object_or_404(Question, pk=question_pk)
    c = get_object_or_404(Choice, question=q, pk=choice_pk)
    if "correct" not in request.session:
        request.session["correct"] = 0
    context = {"question": q, "selected_choice": c}
    request.session["last_question_pk"] = q.pk
    if c.is_correct:
        request.session["correct"] += 1
    return render(request, "quizzes/answer.html", context=context)


# Next question or complete
def next_question(request):
    last_pk = request.session.get("last_question_pk", 0)

    question = Question.objects.filter(pk__gt=last_pk).first()
    if question:
        return redirect("question", pk=question.pk)
    else:
        return redirect("complete")


# Complete the quiz
def complete(request):
    context = {
        "correct": request.session.get("correct", 0),
        "total": request.session.get("total", 0),
    }
    return render(request, "quizzes/complete.html", context=context)


# New game or next question
def new_game(request):
    request.session["last_question_pk"] = 0
    request.session["correct"] = 0
    request.session["total"] = Question.objects.count()
    return redirect("question")
