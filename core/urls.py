from django.urls import path
from .views import index, contato, produtos, clientes, cadastraClientes, salvaClientes
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views


    # suas outras rotas...

urlpatterns = [
    path('', index, name="urlindex"),
    path('contato', contato, name="urlcontato"),
    path('produtos', produtos, name="urlprodutos"),
    path('clientes', clientes, name="urlclientes"),
    path('cadastraClientes', cadastraClientes, name="urlcadastraClientes"),
    path('salvaClientes', salvaClientes, name="urlsalvaClientes"),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('login/', auth_views.LoginView.as_view(template_name='entrar.html'), name='login'),
    path('entrar/', auth_views.LoginView.as_view(template_name='entrar.html'), name='entrar'),  # rota extra
]