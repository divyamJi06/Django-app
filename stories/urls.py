from . import views
from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from .views import WebStoryViewSet

# router = DefaultRouter()
# router.register('create_story', WebStoryViewSet, basename='webstory')

urlpatterns = [
    path('',views.index,name='index'),
    path('create_story/',views.create_story,name='create_story'),
    path("story/<str:link>",views.story,name='story'),
]
