from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('list-country/',views.get_context_data, name='country'),
    path('list-country/<str:letter>',views.get_letter, name='country'),
    path('list-language',views.get_context_data2, name='language'),
    path('country/<str:country>/', views.get_coun, name='con'),
    path('languages/<str:languages>/', views.get_lang, name='lan'),
]
