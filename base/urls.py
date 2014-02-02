"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^login$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^api/hospital/(?P<year>\d{4})/(?P<month>\d{2})/$','hospital',name="jospital"),
    url(r'^ajaxtest$','ajaxtest',name="ajaxtest"),
)
