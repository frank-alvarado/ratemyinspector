from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #Main app
    url(r'^', include('inspectors.urls')),

    #All Auth URLS
    url(r'^accounts/', include('allauth.urls')),

    #Admin URLS
    url(r'^admin/', admin.site.urls),
]