
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
