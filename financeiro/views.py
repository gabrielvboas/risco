from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import FormView, UpdateView, TemplateView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.base import RedirectView

from forms import * 
from financeiro.models import *
from datetime import datetime

from django.views.generic import View
#import pdb; pdb.set_trace()


class json(RedirectView):
    url = reverse_lazy("financeiro:list_conta") # Url para redirecionamento

    def get_redirect_url(self, *args, **kwargs):
        pk_url_kwarg = self.kwargs['pk']

        conta = Conta.objects.filter(pk=pk_url_kwarg)[0]

        conta.conclusao = datetime.now()

        conta.save()

        return super(ConcluirConta, self).get_redirect_url(*args, **kwargs)
    
    def get(self, request):
        return JsonResponse({'teste':'teste'})

class PaginaInicial(TemplateView):
    template_name = 'financeiro/pagina_inicial.html'

class CadastroContaAPagar(FormView):
    template_name = 'financeiro/cadastro_conta_pagar.html' 
    success_url = reverse_lazy('financeiro:lista_conta_pagar')
    form_class = CadastroContaAPagarForm

    def form_valid(self, form):
        conta = ContaAPagar()
        conta.valor = form.cleaned_data['valor']
        conta.vencimento = form.cleaned_data['vencimento']
        conta.fornecedor = form.cleaned_data['fornecedor']
        conta.tipo = ContaAPagar.OUTRAS
        conta.save()

        return HttpResponseRedirect(self.success_url)

class EditarContaAPagar(UpdateView):
    template_name = 'financeiro/cadastro_conta_pagar.html' 
    fields = ['valor', 'vencimento', 'forma_pagamento', 'nome', 'cpf', 'conta', 'agencia', 'banco']
    model = ContaAPagar

    success_url = reverse_lazy('financeiro:lista_conta_pagar')

    def form_valid(self, form):
        conta = form.save(commit=False)
        conta.save()

        return HttpResponseRedirect(self.success_url)

class ConcluirConta(RedirectView):
    url = reverse_lazy('financeiro:lista_conta_pagar') # Url para redirecionamento

    def get_redirect_url(self, *args, **kwargs):
        pk_url_kwarg = self.kwargs['pk']

        conta = ContaAPagar.objects.filter(pk=pk_url_kwarg)[0]

        conta.conclusao = datetime.now()

        conta.save()

        return super(ConcluirConta, self).get_redirect_url(*args, **kwargs)

class CadastroFornecedor(FormView):
    template_name = 'financeiro/cadastro_fornecedor.html'
    form_class = CadastroFornecedorForm
    success_url = reverse_lazy('financeiro:lista_fornecedor')

    def form_valid(self, form):
        supplier = Fornecedor()
        supplier.nome = form.cleaned_data['nome']
        supplier.tipo = form.cleaned_data['tipo']
        supplier.cnpj = form.cleaned_data['cnpj']
        supplier.conta = form.cleaned_data['conta']
        supplier.agencia = form.cleaned_data['agencia']
        supplier.banco = form.cleaned_data['banco']
        supplier.save()

        return HttpResponseRedirect(self.success_url)


class EditarFornecedor(UpdateView):
    template_name = 'financeiro/cadastro_fornecedor.html'
    fields = ['nome', 'tipo', 'cnpj', 'conta', 'agencia', 'banco']
    model = Fornecedor

    success_url = reverse_lazy('financeiro:lista_fornecedor')

    def form_valid(self, form):
        supplier = form.save(commit=False)
        supplier.save()

        return HttpResponseRedirect(self.success_url)

class DeletarFornecedor(RedirectView):
    url = reverse_lazy('financeiro:lista_fornecedor') # Url para redirecionamento

    def get_redirect_url(self, *args, **kwargs):
        pk_url_kwarg = self.kwargs['pk']

        fornecedor = Fornecedor.objects.filter(pk=pk_url_kwarg)[0]

        fornecedor.delete()

        return super(DeletarFornecedor, self).get_redirect_url(*args, **kwargs)

class ItensContaAPagar(ListView):
    template_name = 'financeiro/itens_conta.html'
    model = ProductRequest

    def get_context_data(self, *args, **kwargs):
        context = super(ItensContaAPagar, self).get_context_data(*args, **kwargs)

        pk_url_kwarg = self.kwargs['pk']

        context['items'] = ProductRequest.objects.filter(stockRequest__conta__pk=pk_url_kwarg)

        context['conta'] = ContaAPagar.objects.filter(pk=pk_url_kwarg)

        return context