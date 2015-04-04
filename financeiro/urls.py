from django.conf.urls import patterns, include, url
from financeiro import views
from django.views.generic import list, detail
from financeiro.models import Relatorio, Conta, Cliente


urlpatterns = patterns('',
    url(r'^cadastroconta/', views.CadastroConta.as_view(), name='CadastroConta'),
    url(r'^cadastrocliente/', views.CadastroCliente.as_view(), name='CadastroCliente'),
    url(r'^listacliente', list.ListView.as_view(model=Cliente)),
    url(r'^listaconta', list.ListView.as_view(model=Conta)),
    #url(r'^cliente/(?P<pk>\d+)/$', detail.DetailView.as_view(model=Cliente))
)

