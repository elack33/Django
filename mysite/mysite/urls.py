"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myaccounts import views as myaccounts_views

urlpatterns = [

    # url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url('^', include('django.contrib.auth.urls')),
    url(r'^commentbox/', include('commentbox.urls')),
    url(r'^shirtstore/', include('shirtstore.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^puzzles/', include('puzzles.urls')),
    url(r'^mailinglist/', include('mailinglist.urls')),
    url(r'^registry/', include('registry.urls')),
    url(r'^jobpost/', include('jobpost.urls')),
    url(r'^pizza_maker/', include('pizza_maker.urls')),
    # url(r'^myaccounts/', include([
        # url(r'^(?P<user_id>\d+)/change_password/$', myaccounts_views.change_password, name='change_password')
        url(r'^create_user/$', myaccounts_views.create_user, name='create_user'),
]
# no dollar sign at the end, so make sure names are unique, accounts and accountsforyou are the same

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
