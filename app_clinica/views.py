from rest_framework import viewsets
from .models import Funcionario, Cliente, Fornecedor, Produto
from .serializers import FuncionarioSerializer, ClienteSerializer, FornecedorSerializer, ProdutoSerializer

from django.shortcuts import render
from rest_framework.permissions import AllowAny

class SuaViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]


# Views para renderização de HTML
def funcionarios_view(request):
    return render(request, 'app_clinica/funcionarios.html')

def clientes_view(request):
    return render(request, 'app_clinica/clientes.html')

def fornecedores_view(request):
    return render(request, 'app_clinica/fornecedores.html')

def produtos_view(request):
    return render(request, 'app_clinica/produtos.html')

def index_view(request):
    return render(request, 'app_clinica/index.html')

# API ViewSets
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
