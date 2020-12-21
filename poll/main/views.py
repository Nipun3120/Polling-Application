from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    FormView, 
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from main import models, forms
# Create your views here.

class Index(ListView):
    model = models.Question
    template_name = 'main/index.html'


class Question(PermissionRequiredMixin, SingleObjectMixin, FormView):
    model = models.Question
    template_name = 'main/question.html'
    form_class = forms.AnswerForm



    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['user_answer'] = models.Question.objects.get(
        #     question = self.get_object(),
        #     user = self.request.user,
        # )
        # return data
        print('data -> ')
        print(data)

        
    def form_valid(self, form):

        # If the form is valid, save the associated model
        form_object = form.save(commit = False)
        form_object.question = self.get_object()
        form_object.user = self.request.user
        form_object.save()
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object = self.get_object)
        return self.render_to_response(context)


