
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from atendimento.views import site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('atendimento.urls')),
 
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
