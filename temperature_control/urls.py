from django.conf.urls import patterns, include, url

urlpatterns = patterns('temperature_control.views',
    url(r'^$', 'temperature'),
    url(r'^log/(?P<size>\d{1,})', 'temp_log', name='temp_log'),
    url(r'^set/', 'set_temp', name='set_temp'),)
