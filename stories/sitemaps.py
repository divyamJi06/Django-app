# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import WebStory

class WebStorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    # protocol = 'http'

    def items(self):
        return WebStory.objects.all()

    def location(self, obj: WebStory):
        return '/story/%s' % (obj.permalink)

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['index', 'about', 'contact']

    def location(self, item):
        return reverse(item)