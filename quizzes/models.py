from django.db import models
from django.urls import reverse


class Question(models.Model):
    text = models.CharField("question", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("questions:question", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Question: {self.text}"

    def __repr__(self):
        return f"Question ({self.pk}): {self.text}"

    class Meta:
        ordering = ("pk",)
        verbose_name = "Question"
        verbose_name_plural = "Quiz Questions"


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",
    )
    text = models.TextField("choice")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Choice: {self.text}"

    def __repr__(self):
        return f"Choice ({self.pk}): {self.text}"
