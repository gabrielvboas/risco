# -*- coding: utf-8 -*-
from django import forms
from models import Conta, Fornecedor

class CadastroContaAPagarForm (forms.Form):
	valor = forms.FloatField(required=False, label='Valor')
	vencimento = forms.DateTimeField(required=False, label='Vencimento(mm/dd/aaaa)')
	fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects)

class CadastroFornecedorForm (forms.Form):
	tipo = forms.ChoiceField(choices=Fornecedor.TYPES, label='Tipo')
	nome = forms.CharField(max_length=200, label='Nome')
	cnpj = forms.CharField(max_length=200, label='CNPJ')
	conta = forms.CharField(max_length=200, label='Conta')
	agencia = forms.CharField(max_length=200, label='Agência')
	banco = forms.CharField(max_length=200, label='Banco')

class RequisicaoRelatorioForm (forms.Form):
	data_inicio = forms.CharField(max_length=200, label='Inicio(mm/dd/aaaa)')
	data_fim = forms.CharField(max_length=200, label='Fim(mm/dd/aaaa)')
	