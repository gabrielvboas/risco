# -*- coding: utf-8 -*-
from django import forms
from models import Conta, Fornecedor

class CadastroContaAPagarForm (forms.Form):
	valor = forms.IntegerField(required=False, label='Valor')
	vencimento = forms.DateTimeField(required=False, label='Vencimento(dd/mm/aaaa)')
	fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects)

class CadastroFornecedorForm (forms.Form):
	tipo = forms.ChoiceField(choices=Fornecedor.TYPES, label='Tipo')
	nome = forms.CharField(max_length=200, label='Nome')
	cnpj = forms.CharField(max_length=200, label='CNPJ')
	conta = forms.CharField(max_length=200, label='Conta')
	agencia = forms.CharField(max_length=200, label='Agência')
	banco = forms.CharField(max_length=200, label='Banco')