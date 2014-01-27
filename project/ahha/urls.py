from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^test$', views.test, name='test'),
                       url(r'^logout$', views.logout_user, name='logout'),
                       url(r'^login$', views.login_user, name='login'),

                       )

