from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^pizza/$', views.pizza, name='pizza'),
    url(r'^view_pizza/$', views.viewPizza, name='view_pizza'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)