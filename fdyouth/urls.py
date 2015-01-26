from django.conf.urls import patterns, url

from fdyouth import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'^index', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^contact', views.contact, name='contact'),
        url(r'^overview', views.overview, name='overview'),
        url(r'^add_statu', views.add_statu, name='add_statu'),
        url(r'^add_academy', views.add_academy, name='add_academy'),
        url(r'^add_life', views.add_life, name='add_life'),
        url(r'^add_news', views.add_news, name='add_news'),
        url(r'^add', views.add, name='add'),
        url(r'^search_result', views.search_result, name='search_statu'),
        url(r'^search_life', views.search_life, name='search_life'),
        url(r'^search_academy', views.search_academy, name='search_academy'),
        url(r'^search_news', views.search_news, name='search_news'),
        url(r'^search', views.search, name='search'),
        url(r'^details', views.details, name='details'),
        url(r'^download', views.download, name='downlaod')
                      )
