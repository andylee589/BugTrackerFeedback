from django.conf.urls import patterns, url
from Feedback import views


urlpatterns = patterns("",
       url(r'^$', views.index, name="index"),
       url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
       url(r'^post/$', views.post, name='post')
)