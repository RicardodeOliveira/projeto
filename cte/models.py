from django.db import models

class Lancamento(models.Model):
    cte = models.IntegerField()
    cliente = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    emissao = models.DateField()
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    frete = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.cliente + ' ' + self.estado + ' ' + self.cidade