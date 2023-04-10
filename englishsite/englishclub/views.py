import random

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, TemplateView, FormView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from englishclub.forms import *
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from englishclub.utils import *
from englishclub.models import *


def mainpage(request):
    return render(request, 'englishclub/main.html')


class RegisterUser(CreateView, DataMixin):
    form_class = RegisterUserForm
    template_name = 'englishclub/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_context(title='Регистрация')
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'englishclub/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_context(title='Авторизация')
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class Vocabulary(CreateView):
    form_class = VocabularyForm
    template_name = 'englishclub/Vocabulary.html'

    def form_valid(self, form):  # автозаполнение поля userid текущим пользователем
        object = form.save(commit=False)
        object.userid = self.request.user
        object.save()
        return super(Vocabulary, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dict')


class ShowVocabulary(ListView):
    model = VocabularyModel
    template_name = 'englishclub/register1.html'
    context_object_name = 'dict'

    def get_queryset(self):
        user = self.request.user
        return VocabularyModel.objects.filter(userid=user)



class TestWord(CreateView):
    form_class = WordsForm
    template_name = 'englishclub/words.html'

    def get_success_url(self):
        return reverse_lazy('test')


    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.UserID=self.request.user
        obj.save()
        return super(TestWord,self).form_valid(form)


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        w1=random.choice([x for x in VocabularyModel.objects.filter(userid=self.request.user).values_list('en',flat=True)])
        w2=WordsForm.objects.filter(UserID=self.request.user).values_list('en',flat=True)
        context['test']=w1
        context['w2']=w2

        return context