from django.contrib import admin

# Register your models here.
from .models import Funcionario, Cliente, Fornecedor, Produto

admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Produto)