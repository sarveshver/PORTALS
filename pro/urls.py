
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from same import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',v.same,name='mail')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)