
from django.contrib import admin
from django.urls import path, include
#ativando novamente o projeto

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('galeria.urls')),
]
