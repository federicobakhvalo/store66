import random

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, TemplateView, FormView,View
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from englishclub.forms import *
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from englishclub.utils import *
from englishclub.models import *
from englishclub.utils import Quote


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


class TestWord(FormView):
    template_name = 'englishclub/words.html'
    form_class = WordForm
    trans=str()
    translation_form=[]
    en=[]
    ru=[]

    def form_valid(self, form):
        self.trans=form.cleaned_data.get('translate').lower()
        self.translation_form.append(self.trans)


        return super(TestWord,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        w1=[x for x in VocabularyModel.objects.filter(userid=self.request.user).values_list('en',flat=True)]
        random.shuffle(w1)
        context['word']=w1[0]
        self.en.append(context['word'])
        w2 = VocabularyModel.objects.filter(Q(userid=5) & Q(en=context['word'])).values_list('ru', flat=True)[0]
        self.ru.append(w2)
        return context

    def get_success_url(self):
        return reverse_lazy('test')



class ShowResult(TemplateView,TestWord):
    template_name = 'englishclub/showResult.html'
    def get_context_data(self, **kwargs):
        true_list=[]
        ru=[]
        en=[]
        form=[]
        context=super().get_context_data(**kwargs)
        for i in range(len(self.translation_form)):
            ru.append(self.ru[i])
            en.append(self.en[i])
            form.append(self.translation_form[i])
            if self.translation_form[i]==self.ru[i]:
                true_list.append(True)
            else:
                true_list.append(False)


        context['test']=true_list
        context['en']=en
        context['ru']=ru
        context['deal']=form
        context['zip']=zip(en,ru,form,true_list)


        self.translation_form.clear()
        self.en.clear()
        self.ru.clear()
        return context


