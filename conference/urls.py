from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.view_cnf,name='cnf'),
    url(r'^buy_ticket', views.buy_ticket)
]