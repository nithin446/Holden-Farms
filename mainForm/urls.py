from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.pig_form, name='index'),
    url(r'^submissions/$', views.farm_submissions, name='farm_submissions'),
    url(r'^login/$', auth_views.login, {'template_name': 'mainForm\login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/login/'}, name='logout'),
]