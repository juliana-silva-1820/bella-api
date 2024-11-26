from django.urls import path, include
from .views import funcionarios_view, clientes_view, fornecedores_view, produtos_view, index_view, FuncionarioViewSet, ClienteViewSet, FornecedorViewSet, ProdutoViewSet
from rest_framework.routers import DefaultRouter

# Roteamento de APIs
router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', index_view, name='index'),
    path('index/', index_view, name='index'),
    path('funcionarios/', funcionarios_view, name='funcionarios'),
    path('clientes/', clientes_view, name='clientes'),
    path('fornecedores/', fornecedores_view, name='fornecedores'),
    path('produtos/',produtos_view, name='produtos'),
    path('api/', include(router.urls)),
]
