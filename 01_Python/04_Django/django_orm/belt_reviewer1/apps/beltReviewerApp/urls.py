from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
    url(r'^process$', views.register),
    url(r'^process_login$', views.login),
    url(r'^result$', views.result),
    url(r'^books$', views.books),
    url(r'^add$', views.add),
    url(r'^books/(?P<id>\d+)$', views.reviews),
    url(r'^users/(?P<id>\d+)$', views.users),
    url(r'^book_review$', views.book_review),
    url(r'^new_review/(?P<id>\d+)$', views.new_review),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]