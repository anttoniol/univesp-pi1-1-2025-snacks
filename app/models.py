from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False, blank=False)
    fabricante = models.CharField(max_length=200, null=False, blank=False)
    marca = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    id = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    data_validade = models.DateField("Data de validade", null=False)
    quantidade = models.IntegerField(default=1)

    class Meta:
        unique_together = ('id_produto', 'id_fornecedor', 'data_validade')





