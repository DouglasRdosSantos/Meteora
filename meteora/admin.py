from django.contrib import admin
from meteora.models import Categoria, Produto

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao',)
    list_display_links =('id', 'nome',)
    list_per_page = 20
    ordering = ('nome',)
    search_fields =('nome',)

admin.site.register(Categoria,Categorias)

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'categoria', 'preco', 'imagem')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome', 'categoria',)
    #Optei por 10 para testar, exercicio pedia com 20 por página
    list_per_page = 10
    

admin.site.register(Produto,Produtos)