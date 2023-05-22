from django.conf import urls
from . import views

urlpatterns = [
    urls(r'^$', views.index, name='index'),
]