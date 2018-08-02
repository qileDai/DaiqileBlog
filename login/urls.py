from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [


    url(r'^register/$', views.register, name='login_register'),
    url(r'^loginto/$', views.loginto, name='login_loginto'),
    url(r'^index/',views.index,name='login_index'),
    url(r'^logout/', views.logout,name='login_logout'),
]