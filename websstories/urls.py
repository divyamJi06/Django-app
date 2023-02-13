
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, handler404
handler404 = 'stories.views.handler404'
# handler500 = 'stories.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stories.urls'))
] 
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
