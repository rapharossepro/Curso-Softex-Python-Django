from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin do Django
    path('admin/', admin.site.urls),

    # URLs do app core
    # O include pega as URLs do arquivo acima e adiciona o prefixo 'api/'
    path('api/', include('core.urls')), 
]