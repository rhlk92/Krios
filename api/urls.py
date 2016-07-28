from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^tasks/$', 'task_list_api', name='task_list_api'),
    url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail_api', name='task_detail_api'),
)
