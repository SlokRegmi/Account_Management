from django.urls import path
from . import views
urlpatterns = [
path('', views.login, name='login'),
path ('login', views.login, name='login'),
path ('logout', views.logout, name='logout'),
path ('check', views.check, name='check'),

path ('account/<str:uname>', views.account, name='account'),
path ('search/<str:user>', views.search, name='search'),
path ('signup', views.signup, name='signup'),
path ('changeup', views.changeup, name='changeup'),
path ('update', views.update, name='update'),


]