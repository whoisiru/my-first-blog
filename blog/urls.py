from django.conf.urls import url
from . import views # " . " means import from the same directory

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
