from django.conf.urls import url
from . import views

app_name = 'dev'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stockinfo/(?P<ticker>[A-Za-z\- ]+)/$', views.stockinfo, name = 'stockinfo'),
    url(r'^stockinfo/(?P<ticker>[a-z\- ]+)/$', views.stockinfo, name = 'stockinfo'),
    url(r'^stockinfo/$', views.stockinfo, name = 'stockinfo'),
    url(r'^form/(?P<ticker>[A-Za-z\- ]+)/$', views.form, name = 'form'),
    url(r'^form/(?P<ticker>[a-z\- ]+)/$', views.form, name = 'form'),
    url(r'^form/$', views.form, name = 'form'),
    url(r'^homepage/$', views.homepage, name = 'homepage'),
    #url(r'^form/(?P<ticker>[a-z\- ]+)/$', views.form, name = 'form'),
    #url(r'^form/$', views.form, name = 'form'),
    #url(r'^static/$', 'django.views.static.serve',{'document_roots':settings.STATIC_ROOT},name="media"),
    # url(r'^pic/(?P<stock>[a-z\- ]+)/$', views.pic, name = 'pic'),
    # url(r'^pic/(?P<stock>[A-Za-z\- ]+)/$', views.pic, name = 'pic'),

]
