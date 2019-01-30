from django.conf.urls import url
from jobs import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^data/$', views.datapage, name='data'),
]