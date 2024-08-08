from django.contrib import admin
from django.utils.html import format_html

from .models import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)
