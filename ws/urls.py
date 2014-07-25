'''
Created on Jun 27, 2014

@author: hieunguyen
'''
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from ws import views

urlpatterns = patterns('',
    url(r'^cards/$', views.CardList.as_view()),
    url(r'^decks/$', views.DeckList.as_view()),
    url(r'^sets/$', views.SetList.as_view()),
    url(r'^deck/$', views.DeckDetail.as_view()),
    url(r'^card/$', views.CardDetail.as_view()),
    url(r'^set/$', views.SetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)