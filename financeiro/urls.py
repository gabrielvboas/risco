from django.conf.urls import patterns, include, url
from financeiro import views
from django.views.generic import list, detail
from financeiro.models import Relatorio, Conta, Cliente


urlpatterns = patterns('',
    url(r'^cadastroconta/', views.CadastroConta.as_view(), name='create_conta'),
    url(r'^cadastrocliente/', views.CadastroCliente.as_view(), name='create_cliente'),
    url(r'^listacliente', list.ListView.as_view(model=Cliente), name='list_cliente'),
    url(r'^listaconta', list.ListView.as_view(model=Conta), name='list_conta'),
    url(r'^editconta/(?P<pk>\d+)/$', views.EditarConta.as_view(), name='edit_conta'),
    url(r'^finalizeconta/(?P<pk>\d+)/$', views.ConcluirConta.as_view(), name='finalize_conta'),
    url(r'^meujson/', views.json.as_view(), name='json'),
    #url(r'^cliente/(?P<pk>\d+)/$', detail.DetailView.as_view(model=Cliente))
)
