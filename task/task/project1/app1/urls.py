from django.urls import path
from . import views

urlpatterns= [
    path('index/',views.index,name='index'),
    path('index/about/',views.about,name='about'),
    path('index/login/',views.login,name='login'),
    path('index/contact/',views.contact,name='contact'),
]