from django.db import models
from datetime import datetime

# Create your models here.
class Receita(models.Model):
    titulo_receita = models.CharField(max_length=200);
    resumo_receita = models.CharField(max_length=255, default='')
    tempo_receita = models.CharField(max_length=200, default='');
    rendimento_receita = models.CharField(max_length=200, default='');
    imagem_preview = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='static/default_image.png')
    conteudo_receita = models.TextField();
    data_receita = models.DateTimeField('Data publicação', default=datetime.now());

    def __str__(self):
        return self.titulo_receita;

class Produto(models.Model):
    nome = models.CharField(max_length=200);
    descricao = models.TextField()
    # desc = models.TextField()
    imagem = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='static/default_image.png')

    info1 = models.CharField(max_length=255, default='', blank=True)
    cod1 = models.CharField(max_length=255, default='', blank=True)
    info2 = models.CharField(max_length=255, default='', blank=True)
    cod2 = models.CharField(max_length=255, default='', blank=True)
    info3 = models.CharField(max_length=255, default='', blank=True)
    cod3 = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.nome;
