from . import views
from django.urls import path,include
# from .sitemaps import WebStorySitemap/
from .sitemaps import WebStorySitemap,StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
# from rest_framework.routers import DefaultRouter
# from .views import WebStoryViewSet

# router = DefaultRouter()
# router.register('create_story', WebStoryViewSet, basename='webstory')

sitemaps = {
    'story': WebStorySitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('create_story/',views.create_story,name='create_story'),
    path('contact_submit/',views.contact_submit,name='contact_submit'),
    path("story/<str:link>",views.story,name='story'),
    path("sitemap.xml",sitemap,{'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",views.robots,name='robots'),
]