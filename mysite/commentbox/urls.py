from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^comment_return', views.comment_page, name='comment_return'),
]
