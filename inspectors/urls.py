from django.conf.urls import url

from . import views

app_name = 'inspectors'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]