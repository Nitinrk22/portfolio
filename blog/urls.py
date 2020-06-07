"""This is Blog URLS, when we are redirected from Main urls.py """


from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblog, name ='allblog'),
    path('<int:blogid>', views.detail, name ='detail'),

]
