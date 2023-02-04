from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import WebStoryViewSet

router = DefaultRouter()
# router.register('create_story', WebStoryViewSet, basename='webstory')

urlpatterns = [
    path('',views.index,name='index'),
    path('create_story/',views.create_story,name='create_story'),
    # path('create_story/',views.create_web_story,name='create_story'),
    path("story/<str:link>",views.story,name='story'),
    path('', include(router.urls)),
    # path("create_story",views.WebStoryViewSet.as_view(),name='create_story'),
    # path("create_story",views.WebStoryViewSet.as_view(),name='create_story'),
    # path(r'^story/(?P<id>[0-9]+)/$',views.story,name='story')
    # r'^link/(?P<id>[0-9]+)/$''
]
