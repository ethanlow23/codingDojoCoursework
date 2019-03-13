from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^users$', views.index),     # This line has changed!
	url(r'new$', views.new),
	url(r'(?P<id>\d+)/edit$', views.edit),
	url(r'^users/(?P<id>\d+)', views.show),
	url(r'^users/create$', views.create),
	url(r'(?P<id>\d+)/destroy$', views.destroy),
	url(r'(?P<id>\d+)/update$', views.update)
]