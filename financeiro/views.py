from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import FormView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.base import RedirectView

from forms import CadastroContaForm 
from forms import CadastroClienteForm 
from financeiro.models import Conta
from financeiro.models import Cliente
from datetime import datetime

#import pdb; pdb.set_trace()

class CadastroConta(FormView):
    template_name = 'financeiro/cadastroconta.html'
    form_class = CadastroContaForm 
    success_url = reverse_lazy('financeiro:create_conta')

    def form_valid(self, form):
        conta = Conta()
        conta.valor = form.cleaned_data['valor']
        conta.tipo = form.cleaned_data['tipo']
        conta.valor = form.cleaned_data['valor']
        conta.vencimento = form.cleaned_data['vencimento']
        conta.forma_pagamento = form.cleaned_data['forma_pagamento']
        conta.nome = form.cleaned_data['nome']
        conta.cpf = form.cleaned_data['cpf']
        conta.conta = form.cleaned_data['conta']
        conta.agencia = form.cleaned_data['agencia']
        conta.banco = form.cleaned_data['banco']
        conta.save()

        return HttpResponseRedirect(self.success_url)


class CadastroCliente(FormView):
    template_name = 'financeiro/CadastroCliente.html'
    form_class = CadastroClienteForm 
    success_url = reverse_lazy('financeiro:create_clente')

    def form_valid(self, form):
        cliente = Cliente()
        cliente.tipo = form.cleaned_data['tipo']
        cliente.nome = form.cleaned_data['nome']
        cliente.cnpj = form.cleaned_data['cnpj']
        cliente.conta = form.cleaned_data['conta']
        cliente.agencia = form.cleaned_data['agencia']
        cliente.banco = form.cleaned_data['banco']
        cliente.save()

        return super(CadastroCliente, self).form_valid(form)

class EditarConta(UpdateView):
    template_name = 'financeiro/CadastroConta.html'
    #form_class = CadastroContaForm 
    fields = ['valor', 'tipo', 'vencimento', 'forma_pagamento', 'nome', 'cpf', 'conta', 'agencia', 'banco']
    model = Conta

    success_url = reverse_lazy('financeiro:list_conta')

    def form_valid(self, form):
        conta = form.save(commit=False)
        conta.save()

        return HttpResponseRedirect(self.success_url)

class ConcluirConta(RedirectView):
    url = reverse_lazy("financeiro:list_conta") # Url para redirecionamento

    def get_redirect_url(self, *args, **kwargs):
        pk_url_kwarg = self.kwargs['pk']

        conta = Conta.objects.filter(pk=pk_url_kwarg)[0]

        conta.conclusao = datetime.now()

        conta.save()

        return super(ConcluirConta, self).get_redirect_url(*args, **kwargs)