import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text

    def wasPublishedRecently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Cliente(models.Model):
    CPF = models.CharField(max_length=14)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=35)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    CEP = models.CharField(max_length=8)
    foneResidencial = models.CharField(max_length=15)
    fonteTrabalho = models.CharField(max_length=15)
    rendaFamiliar = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.CharField(max_length=35)

    def __str__(self):
        return "%s - %s" % (self.nome, self.CPF)

class Venda(models.Model):
    dataVenda = models.DateTimeField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return "Cliente: %s - Valor: %.2f" % (self.cliente.nome, self.valorTotal)

class Produto(models.Model):
    nome = models.CharField(max_length=35)
    quantidade = models.IntegerField()
    minQuantidade = models.IntegerField()
    
    def __str__(self):
        return "%s - %d" % (self.nome, self.quantidade)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return "Venda (%d) - Produto (%s) - Quantidade: %d - Valor total: %.2f" % (self.venda.id, self.produto.nome, self.quantidade, self.quantidade * self.precoUnitario)

class Fornecedor(models.Model):
    CNPJ = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=35)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    CEP = models.CharField(max_length=8)
    telefone = models.CharField(max_length=15)
    responsavel = models.CharField(max_length=30)
    website = models.CharField(max_length=80)

    def __str__(self):
        return "%s - %s" % (self.nome, self.CNPJ)

class Pedido(models.Model):
    dataPedido = models.DateField()
    dataRecebimento = models.DateField()
    precoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return "Fornecedor: %s - Preco total :%.2f" % (self.fornecedor, self.precoTotal)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido)
    produto = models.ForeignKey(Produto)
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return "Pedido (%d) - Produto (%s) - Quantidade: %d - Valor total: %.2f" % (self.pedido.id, self.produto.nome, self.quantidade, self.quantidade * self.precoUnitario)
