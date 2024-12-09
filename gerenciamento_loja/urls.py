from django.contrib import admin
from django.urls import path, include
from loja.views import tela_inicial  # Importando a nova view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', include('loja.urls')),
    path('', tela_inicial, name="tela_inicial"),  # Redireciona para a nova tela inicial
]
