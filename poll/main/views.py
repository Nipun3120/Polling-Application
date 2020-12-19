from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)


from main import models

# Create your views here.

class Index(ListView):
    model = models.Question
    template_name = 'main/index.html'


class Question(DetailView):
    model = models.Question
    template_name = 'main/question.html'