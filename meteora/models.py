from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

class Categoria(models.Model):
    nome = models.CharField(blank=False, max_length= 100)
    descricao = models.CharField(blank=True, max_length= 500)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length = 255, blank=False, null=False)
    descricao = models.CharField(max_length = 1000,blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0.00)])
    quantidade_estoque = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    categoria = models.ForeignKey(Categoria, blank=False, on_delete=models.CASCADE, null=False) 
    imagem = models.ImageField(upload_to='Produtos/%Y/%m/%d/', blank=True, null=True, )
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome


