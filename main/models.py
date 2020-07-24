from django.db import models
from datetime import datetime

# Create your models here.
class Receita(models.Model):
    titulo_receita = models.CharField(max_length=200);
    resumo_receita = models.CharField(max_length=255, default='')
    imagem_preview = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='static/default_image.png')
    conteudo_receita = models.TextField();
    data_receita = models.DateTimeField('Data publicação', default=datetime.now());

    def __str__(self):
        return self.titulo_receita;

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200);
    desc_produto = models.CharField(max_length=255, default='')
    imagem_produto = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='static/default_image.png')

    def __str__(self):
        return self.nome_produto;
