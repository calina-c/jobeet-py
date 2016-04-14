from django.conf.urls import url
from jobeet import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^job/list$', views.JobList.as_view(), name='job_list'),
    url(r'^job/new$', views.JobCreate.as_view(), name='job_new'),
    url(r'^job/edit/(?P<pk>\d+)$', views.JobUpdate.as_view(), name='job_edit'),
    url(
        r'^job/delete/(?P<pk>\d+)$',
        views.JobDelete.as_view(),
        name='job_delete'
    ),
]
