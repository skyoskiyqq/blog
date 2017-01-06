# -*-coding:utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.apps import apps as django_apps
from blogpost.models import Blogpost

class BlogpostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5
    
    def items(self):
        return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.posted

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1
    
    def items(self):
        return ['home']

    def location(self, obj):
        return reverse(obj)

class FlatPageSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.8
    
    def items(self):
        Site = django_apps.get_model('sites.Site')
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter(registration_required=False)