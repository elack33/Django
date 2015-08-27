from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<wedding_id>\d+)/purchase/$', views.purchase, name='purchase'),
    url(r'^add_gift/$', views.add_gift, name='add_gift'),
]