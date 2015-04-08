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
	valor = models.IntegerField() # saldo devedor
	vencimento = models.DateTimeField()
	forma_pagamento = models.CharField(max_length=200)
	nome = models.CharField(max_length=200)
	cpf = models.CharField(max_length=200)
	conclusao = models.DateTimeField(null=True, blank=True, default = None)
	conta = models.CharField(max_length=200)
	agencia = models.CharField(max_length=200)
	banco = models.CharField(max_length=200)
	id_relatorio = models.ForeignKey(Relatorio, null=True, blank=True, default = None)
	
	def __str__(self):
		return self.nome + "_" + str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')

class Cliente(models.Model):
	ALIMENTICIO = 'ALIMENTICIO'
	MANUTENCAO = 'MANUTENCAO'
	TRIVIAL = 'TRIVIAL'

	TYPES = (
		(ALIMENTICIO, "Alimenticio"),
		(MANUTENCAO, "Manutencao"),
		(TRIVIAL, "Trivial"),
		)
	tipo = models.CharField(choices=TYPES, max_length=50)
	nome = models.CharField(max_length=200)
	cnpj = models.CharField(max_length=200)
	conta = models.CharField(max_length=200)
	agencia = models.CharField(max_length=200)
	banco = models.CharField(max_length=200)
	id_relatorio = models.ForeignKey(Relatorio, null=True, blank=True, default = None)
	
	def __str__(self):
		return self.nome + "_" + str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')


#####################################
# Classes Externas - via WebService #
#####################################

# Objetos serao instanciados atraves da comunicacao com o modulo "GITT Hotel"
class CheckoutPayment(models.Model):
	
	# CARTAODECREDITO = 'CARTAODECREDITO' # Codigo 0
	# CARTAODEDEBITO = 'CARTAODEDEBITO' # Codigo 1
	# CHEQUE = 'CHEQUE' # Codigo 2
	# PAGAMENTOEMDINHEIRO = 'PAGAMENTOEMDINHEIRO' # Codigo 3

	# TYPES = (
	# 	(CARTAODECREDITO, "CARTAODECREDITO"),
	# 	(CARTAODEDEBITO, "CARTAODEDEBITO"),
	# 	(CHEQUE, "CHEQUE"),
	# 	(PAGAMENTOEMDINHEIRO, "PAGAMENTOEMDINHEIRO"),
	# 	)

	cpf = models.CharField(max_length=200)
	valor_pagamento = models.IntegerField()
	data_pagamento = models.DateTimeField(null=True, blank=True, default = None)
	tipo_pagamento = models.IntegerField()

	def __str__(self):
		return self.cpf + "_" + str(self.id)


# Objetos serao instanciados atraves da comunicacao com o modulo "Contumacia"
class Reservation(models.Model)	:
	
	nome = models.CharField(max_length=200)
	cpf = models.CharField(max_length=200)
	valor_reserva = models.IntegerField()	#representa apenas o valor referente aos 10% da reserva
	data_inicio_reserva = models.DateTimeField(null=True, blank=True, default = None)
	data_fim_reserva = models.DateTimeField(null=True, blank=True, default = None)

	
	#Como instanciar uma nova conta a receber?
	id_conta = models.ForeignKey(Conta, null=True, blank=True, default = None)

	def __str__(self):
		return self.cpf + "_" + str(self.id)


# Objetos serao instanciados atraves da comunicacao com o modulo "PEDREIRO HOTELS"
class StockRequest(models.Model):

	PAGO = 'PAGO'
	PENDENTE = 'PENDENTE'
	REPROVADO = 'REPROVADO'

	TYPES = (
		(PAGO, "PAGO"),
		(PENDENTE, "PENDENTE"),
		(REPROVADO, "REPROVADO"),
		)

	status = models.CharField(choices=TYPES, max_length=50)
	data_requisicao = models.DateTimeField(null=True, blank=True, default = None)

	def __str__(self):
		return self.data_requisicao + "_" + str(self.id) + "_" + self.status

class ProductRequest(models.Model):

	id_produto = models.IntegerField()
	valor = models.IntegerField()
	quantidade = models.IntegerField()

	def __str__(self):
		return self.id_produto + "_" + str(self.id) + "_" + self.quantidade