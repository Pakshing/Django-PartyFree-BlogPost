from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'APP_01_PartyFree'

urlpatterns=[
    path('',views.index,name='index'),
    path('new/', views.index_new,name='index_new')
]
