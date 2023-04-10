from django.urls import path,include
from englishclub.views import *
urlpatterns = [

    path('',mainpage,name='home'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('dictionary/',Vocabulary.as_view(),name='dict'),
    path('show/',ShowVocabulary.as_view(),name='show'),
    path('test/',TestWord.as_view(),name='test')



]