from django.db import models

class Relatorio(models.Model):
	aprovado = models.BooleanField(default=False)
	data = models.DateTimeField()
	
	def __str__(self):
		return self.nome + "_" + str(self.id) + + "_" + self.data.strftime('%d/%m/%y')

class Conta(models.Model):
	PAGAR = 'PAGAR'
	RECEBER = 'RECEBER'

	TYPES = (
		(PAGAR, "Pagar"),
		(RECEBER, "Receber"),
		)
	tipo = models.CharField(choices=TYPES, max_length=50) #0 para conta a receber - 1 para conta a pagar
	valor = models.IntegerField()
	vencimento = models.DateTimeField()
	forma_pagamento = models.CharField(max_length=200)
	nome = models.CharField(max_length=200)
	cpf = models.CharField(max_length=200)
	conclusao = models.DateTimeField()
	conta = models.CharField(max_length=200)
	agencia = models.CharField(max_length=200)
	banco = models.CharField(max_length=200)
	id_relatorio = models.ForeignKey(Relatorio, null=True, blank=True, default = None)
	
	def __str__(self):
		return self.nome + "_" + str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')

