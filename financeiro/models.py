from django.db import models

class Relatorio(models.Model):
	aprovado = models.BooleanField(default=False)
	data = models.DateTimeField()
	
	def __str__(self):
		return self.nome_beneficiario + "_" + str(self.id) + + "_" + self.data.strftime('%d/%m/%y')

class ContaAPagar(models.Model):
	valor = models.IntegerField()
	vencimento = models.DateTimeField()
	forma_pagamento = models.CharField(max_length=200)
	nome_beneficiario = models.CharField(max_length=200)
	cpf_beneficiario = models.CharField(max_length=200)
	conclusao = models.DateTimeField()
	conta_destino = models.CharField(max_length=200)
	agencia_destino = models.CharField(max_length=200)
	banco_destino = models.CharField(max_length=200)
	id_relatorio = models.ForeignKey(Relatorio, null=True, blank=True, default = None)
	
	def __str__(self):
		return self.nome_beneficiario + "_" + str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')


class ContaAReceber(models.Model):
	valor = models.IntegerField()
	vencimento = models.DateTimeField()
	forma_pagamento = models.CharField(max_length=200)
	nome_devedor = models.CharField(max_length=200)
	cpf_devedor = models.CharField(max_length=200)
	conclusao = models.DateTimeField()
	conta_origem = models.CharField(max_length=200)
	agencia_origem = models.CharField(max_length=200)
	banco_origem = models.CharField(max_length=200)
	id_relatorio = models.ForeignKey(Relatorio, null=True, blank=True, default = None)
	
	def __str__(self):
		return self.nome_devedor + "_" + str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')