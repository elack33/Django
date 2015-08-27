from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^job_post/$', views.job_post, name='job_post'),
    url(r'^view_jobs/$', views.view_jobs, name='view_jobs'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^logout/$', views.logout_view, name='logout'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)