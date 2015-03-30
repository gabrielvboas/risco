from django import forms

from models import Conta

class CadastroConta (forms.Form):
	tipo = forms.ChoiceField(choices=Conta.TYPES, label='tipo')
	valor = forms.IntegerField(required=False, label='valor')
	vencimento = forms.DateTimeField(required=False, label='vencimento')
	forma_pagamento = forms.CharField(label='forma_pagamento')
	nome = forms.CharField(max_length=200, label='nome')
	cpf = forms.CharField(max_length=200, label='cpf')
	conclusao = forms.DateTimeField(label='conclusao')
	conta = forms.CharField(max_length=200, label='conta')
	agencia = forms.CharField(max_length=200, label='agencia')
	banco = forms.CharField(max_length=200, label='banco')