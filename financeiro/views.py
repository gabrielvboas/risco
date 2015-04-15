from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import FormView, UpdateView, TemplateView, ListView, View
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.base import RedirectView

from forms import * 
from financeiro.models import *
from datetime import datetime
from models import Validacao
import urllib2
import json as ehojson

from django.views.generic import View
#import pdb; pdb.set_trace()

def json(request, tipo):
    a = ''
    for obj in Validacao.objects.all():
        if obj.tipo == tipo:
            a = a + obj.to_JSON()

    return JsonResponse(a, safe=False)


def teste(request):
    print "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    html = urllib2.urlopen('http://127.0.0.1:8000/financeiro/json/RESERVA/')
    data = ehojson.load(html)
    data = data.replace("}{","},,{")
    lista = data.split(",,")

    obj_banco = Validacao.objects.all()
    l = list()
    for i in obj_banco:
        l.append(i.idObj)

    for obj in lista:
        data = ehojson.loads(obj)
        a = Validacao()
        a.validacao = data["VALIDACAO"]
        a.tipo = data["TIPO"]
        a.comentario = data["COMENTARIO"]
        a.idObj = data["IDOBJ"]
        if a.idObj not in l:
            a.save()    

    return JsonResponse('html', safe=False)

class postteste(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


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
    fields = ['valor', 'vencimento', 'fornecedor']
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

class RequisicaoRelatorio(FormView):
    template_name = 'financeiro/requisicao_relatorio.html' 
    success_url = reverse_lazy('financeiro:mostra_relatorio')
    form_class = RequisicaoRelatorioForm

    def form_valid(self, form):
        #pegar dados das contas entre as datas

        relat = Relatorio.objects.filter()
        for r in relat:
            r.delete()

        relatorio = Relatorio()

        conta = ContaAPagar.objects.filter(vencimento__gte=datetime.strptime(form.cleaned_data['data_inicio'], '%d/%M/%Y').date(), vencimento__lte=datetime.strptime(form.cleaned_data['data_fim'], '%d/%M/%Y').date(), conclusao__isnull=False)
        saldo = 0

        for item in conta:
            saldo = saldo + item.valor

        relatorio.aprovado = "sim"
        relatorio.saldo = saldo
        relatorio.descricao = "Gastos"
        #import pdb; pdb.set_trace()
        relatorio.save()
        #passar conta para a classe seguinte
        
        #saldo = 0
        #reserva = Reservation.objects.filter(data_inicio_reserva__gte=datetime.strptime(form.cleaned_data['data_inicio'], '%d/%M/%Y').date(), data_inicio_reserva__lte=datetime.strptime(form.cleaned_data['data_fim'], '%d/%M/%Y').date())
        #valor_estadia
        #for item in reserva:
        #    saldo = saldo + reserva.valor_estadia

        #pgtoCheckout = CheckoutPayment.objects.filter(data_pagamento__gte=datetime.strptime(form.cleaned_data['data_inicio'], '%d/%M/%Y').date(), data_pagamento__lte=datetime.strptime(form.cleaned_data['data_fim'], '%d/%M/%Y').date())
        #valor_pagamento 
        #for item in reserva:
        #    saldo = saldo + pgtoCheckout.valor_pagamento        

        #relatorio.aprovado = "sim"
        #relatorio.saldo = saldo
        #relatorio.descricao = "Recebido"

        #relatorio.save()

        return HttpResponseRedirect(self.success_url) 

#class MostraRelatorio(ListView):
#    template_name = 'financeiro/mostra_relatorio.html'
#    model = Relatorio

#    def get_context_data(self, *args, **kwargs):

        #colocar valores da conta na tabela 

#        return #conta
