from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import FormView
from forms import CadastroConta
from financeiro.models import Conta
import time
#import pdb; pdb.set_trace()

class CadastroConta(FormView):
    template_name = 'financeiro/cadastroconta.html'
    form_class = CadastroConta
    success_url = 'financeiro/cadastroconta'

    def form_valid(self, form):
        conta = Conta()
        conta.valor = form.cleaned_data['valor']
        conta.tipo = form.cleaned_data['tipo']
        conta.valor = form.cleaned_data['valor']
        conta.vencimento = form.cleaned_data['vencimento']
        conta.forma_pagamento = form.cleaned_data['forma_pagamento']
        conta.nome = form.cleaned_data['nome']
        conta.cpf = form.cleaned_data['cpf']
        #conta.conclusao = form.cleaned_data['conclusao']
        conta.conta = form.cleaned_data['conta']
        conta.agencia = form.cleaned_data['agencia']
        conta.banco = form.cleaned_data['banco']
        conta.save()

        return super(CadastroConta, self).form_valid(form)