from django.conf import urls
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]