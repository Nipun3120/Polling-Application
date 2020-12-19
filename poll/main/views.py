from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    FormView, 
)
from django.views.generic.detail import BaseDetailView

from main import models, forms

# Create your views here.

class Index(ListView):
    model = models.Question
    template_name = 'main/index.html'


class Question(BaseDetailView, FormView):
    model = models.Question
    template_name = 'main/question.html'
    form_class = forms.AnswerForm

    def form_valid(self, form):

        # If the form is valid, save the associated model
        form_object = form.save(commit = False)
        form_object.user = self.request.user
        form_object.save()

        return HttpResponseRedirect('/')


