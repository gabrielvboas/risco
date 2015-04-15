from django.db import models
import datetime

class Validacao(models.Model):
	RESERVA = 'RESERVA'
	ESTOQUE = 'ESTOQUE'
	GASTOCLIENTE = 'GASTOCLIENTE'
	TYPES = (
		(RESERVA, "Pagar"),
		(ESTOQUE, "Estoque"),
		(GASTOCLIENTE, "GastoCliente"),
		)
	tipo = models.CharField(choices=TYPES, max_length=50)
	idObj = models.IntegerField(default=False)
	#na vdd isso ser'a uma foreing key
	validacao = models.BooleanField(default=False)
	comentario = models.CharField(max_length=200)

	def __str__(self):
		return self.tipo + "_" + str(self.idObj) 

class Relatorio(models.Model):
	aprovado = models.CharField(max_length=200)
	descricao = models.CharField(max_length=200)
	saldo = models.FloatField()
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
		return super(Relatorio, self).save(*args, **kwargs)
	
	def __str__(self):
		return str(self.id) + "_" + self.descricao


class Fornecedor(models.Model):
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
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
		return super(Fornecedor, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.nome

class ContaAPagar(models.Model):
	ESTOQUE = 'ESTOQUE'
	OUTRAS = 'OUTRAS'

	TYPES = (
		(ESTOQUE, "ESTOQUE"),
		(OUTRAS, "OUTRAS"),
		)
	tipo = models.CharField(choices=TYPES, max_length=50)
	valor = models.FloatField()
	vencimento = models.DateTimeField()
	conclusao = models.DateTimeField(null=True, blank=True, default = None)
	relatorio = models.ForeignKey(Relatorio, null=True, blank=True, default = None)
	fornecedor = models.ForeignKey(Fornecedor, null=True, blank=True, default = None)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
		return super(ContaAPagar, self).save(*args, **kwargs)
	
		
	
	def __str__(self):
		return str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')

class Conta(models.Model):
	cpf = models.CharField(max_length=200)
	saldo_devedor = models.FloatField() #9x se reserva ou tudo se checkin
	checkin = models.BooleanField(default=False)
	checkout = models.BooleanField(default=False)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
		return super(Conta, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.nome + "_" + str(self.id) + "_" + self.vencimento.strftime('%d/%m/%y')


############################################################
#             Classes Externas - via WebService            #
############################################################

# Objetos serao instanciados atraves da comunicacao com o modulo "Contumacia"
class Reservation(models.Model)	:
	
	nome = models.CharField(max_length=200)
	cpf = models.CharField(max_length=200)
	valor_reserva = models.IntegerField()	#representa apenas o valor referente aos 10% da reserva
	data_inicio_reserva = models.DateTimeField(null=True, blank=True, default = None)
	data_fim_reserva = models.DateTimeField(null=True, blank=True, default = None)

	conta = models.ForeignKey(Conta)

	def __str__(self):
		return self.cpf + "_" + str(self.id)

# Informacao vira do modulo "GITT"
# Caso ja exista reserva previa, basta atualizar o objeto conta do respectivo CPF
# Caso nao exista reserva previa, deve ser instanciada uma nova conta a receber com essas informacoes
class CheckInConfirmation(models.Model):
	nome = models.CharField(max_length=200)
	cpf = models.CharField(max_length=200)
	valor_estadia = models.IntegerField()	#nao inclui a reserva, equivale aos 100%
	data_check_in = models.DateTimeField(null=True, blank=True, default = None)
	data_check_out = models.DateTimeField(null=True, blank=True, default = None)

	# Linkando com Reserva
	reservation = models.ForeignKey(Reservation, null=True, blank=True, default = None)

	conta = models.ForeignKey(Conta)

	def __str__(self):
		return self.cpf + "_" + str(self.id)

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
	valor_pagamento = models.FloatField()
	data_pagamento = models.DateTimeField(null=True, blank=True, default = None)
	tipo_pagamento = models.IntegerField()

	conta = models.ForeignKey(Conta)

	def __str__(self):
		return self.cpf + "_" + str(self.id)

# Objetos serao instanciados atraves da comunicacao com o modulo "PEDREIRO HOTELS"
# Receberemos uma lista com varias triplas: descricao do produto, valor, quantidade
# Se a conta for aprovada/paga, deve ser instaciada uma conta a pagar
# Deve ser enviada uma mensagem para o modulo "Pedreiro" informando a mudanca de status
# Ou podemos simplesmente ignorar o status, e facilitar essa parte da logica
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

	# Linkando com ContaAPagar
	conta = models.ForeignKey(ContaAPagar)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
		return super(StockRequest, self).save(*args, **kwargs)

	def __str__(self):
		return "_" + str(self.id) + "_" + self.status

# Tripla recebida do modulo "Pedreiros"
# deve estar ligada a uma StockRequest
class ProductRequest(models.Model):

	descricao =  models.CharField(max_length=200)
	valor = models.FloatField()
	quantidade = models.IntegerField()

	# Linkando com StockRequest
	stockRequest = models.ForeignKey(StockRequest)

	def __str__(self):
		return str(self.id) + "_" + str(self.quantidade)