from django.conf.urls import patterns, include, url
from rwfm import views

urlpatterns = patterns('',
    url(r'^rwfm/objects/$', views.object_list),
    url(r'^rwfm/subjects/$', views.subject_list),
    url(r'^rwfm/$', views.home),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
)
