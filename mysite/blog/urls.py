from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page-with-links/$', views.page_with_links, name='page_with_links'),
    url(r'^page-with-links/([0-9]+)/$', views.one_at_a_time, name='single_blog'),
    url(r'^page-with-links/about_page/$', views.about_page, name='about'),

]
# always end the url with a slash