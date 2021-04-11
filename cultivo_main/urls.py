from django.urls import path,include
from . import views
from django.conf.urls import url
from django.views import generic


app_name="cultivo_main"    #called namespacing of urls,,,so as to distinguish between similar named urls 				#of different apps
urlpatterns=[
    path(r'',views.TemplateView.as_view(),name="home"),  #starting Page
    path(r'contact',views.TemplateView2.as_view(),name="contact"),
    path(r'story',views.TemplateView3.as_view(),name="story"),
    path(r'services',views.TemplateView4.as_view(),name="services"),
    # path(r'contactus',views.TemplateView_con.as_view(),name="contact"),

    path(r'result',views.work,name="result"),
    path(r'register', views.register, name='register'),
    path(r'login1', views.login1, name='login1'),
    path(r'input', views.login1, name='input'),
    # path(r'form_signin',views.)
    # path('upload',views.upload,name="upload"),
]