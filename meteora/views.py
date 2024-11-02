from meteora.models import Categoria, Produto
from meteora.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class CategoriaViewSet(viewsets.ModelViewSet):
    '''
    - GET: Retorna uma lista de categorias ou uma categoria específica.
    - POST: Cria uma nova categoria.
    - PUT: Atualiza uma categoria existente.
    - DELETE: Deleta uma categoria.

    **Autenticação**:
    - Apenas usuários autenticados podem acessar este endpoint, utilizando autenticação básica.

    **Limitação de Taxa**:
    - Usuários autenticados: até 50 requisições por dia.
    - Usuários anônimos: até 20 requisições por dia.
    '''
    queryset = Categoria.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriaSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class ProdutoViewSet(viewsets.ModelViewSet):
    '''
    API endpoint para listar, criar, atualizar e deletar produtos.

    **Métodos HTTP suportados**:
    - GET: Retorna uma lista de produtos ou um produto específico.
    - POST: Cria um novo produto.
    - PUT: Atualiza um produto existente.
    - DELETE: Deleta um produto.

    **Autenticação**:
    - Apenas usuários autenticados podem acessar este endpoint, utilizando autenticação básica.

    **Limitação de Taxa**:
    - Usuários autenticados: até 50 requisições por dia.
    - Usuários anônimos: até 20 requisições por dia.

    **Filtros**:
    - `search`: Permite buscar produtos pelo nome, categoria ou preço.
    - Filtros adicionais podem ser aplicados através de parâmetros de consulta.
    '''
    queryset = Produto.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome', 'categoria', 'preco']
    serializer_class = ProdutoSerializer  
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


