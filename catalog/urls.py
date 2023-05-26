from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
]
urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]