from django.conf.urls import patterns, url

from subscribe import views

urlpatterns = patterns('', 
        url(r'^subscribe_statu', views.subscribe_statu, name='subscribe_statu'),
        url(r'^subscribe[^_]', views.subscribe, name='subscribe'),
                      )
