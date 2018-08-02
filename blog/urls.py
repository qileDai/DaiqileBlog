
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [

    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='blog_detail'),
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='blog_archives'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='blog_category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='blog_tag'),
    url(r'^search/$', views.search, name='blog_search'),
    url(r'^login/$', views.login, name='blog_login'),
    url(r'^brotherviews/$', views.brotherviews,name='blog_brotherviews'),
    url(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='comment_reply'),
    url(r'^pythonnotes/$', views.pythonnotes,name='blog_pythonnotes'),
    url(r'^aboutauthor/$', views.aboutauthor, name='blog_aboutauthor'),




]
