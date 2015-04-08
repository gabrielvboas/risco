# -*- coding: utf-8 -*-
from django import forms
from models import Conta
from models import Cliente

class CadastroContaForm (forms.Form):
	tipo = forms.ChoiceField(choices=Conta.TYPES, label='Tipo')
	valor = forms.IntegerField(required=False, label='Valor')
	vencimento = forms.DateTimeField(required=False, label='Vencimento(dd/mm/aaaa)')
	forma_pagamento = forms.CharField(label='Forma de Pagamento')
	nome = forms.CharField(max_length=200, label='Nome')
	cpf = forms.CharField(max_length=200, label='Cpf')
	#conclusao = forms.DateTimeField(label='conclusao(dd/mm/aaaa)') #Conclusao e setada depois
	conta = forms.CharField(max_length=200, label='Conta')
	agencia = forms.CharField(max_length=200, label='Agência')
	banco = forms.CharField(max_length=200, label='Banco')
	#criado_em = forms.DateTimeField('criado em', auto_now_add=True) #pensei em colocar um campo de quando foi adicionado o registro


class CadastroClienteForm (forms.Form):
	tipo = forms.ChoiceField(choices=Cliente.TYPES, label='Tipo')
	nome = forms.CharField(max_length=200, label='Nome')
	cnpj = forms.CharField(max_length=200, label='CNPJ')
	conta = forms.CharField(max_length=200, label='Conta')
	agencia = forms.CharField(max_length=200, label='Agência')
	banco = forms.CharField(max_length=200, label='Banco')