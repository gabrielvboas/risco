from django.conf.urls import patterns, include, url
from financeiro import views
from django.views.generic import list, detail
from financeiro.models import Fornecedor, ContaAPagar, Conta


urlpatterns = patterns('',
	url(r'^$', views.teste, name='initial'),
    url(r'^cadastroconta/', views.CadastroContaAPagar.as_view(), name='criar_conta_pagar'),
    url(r'^listacontapagar', list.ListView.as_view(model=ContaAPagar), name='lista_conta_pagar'),
    url(r'^editconta/(?P<pk>\d+)/$', views.EditarContaAPagar.as_view(), name='edita_conta_pagar'),
    url(r'^itensconta/(?P<pk>\d+)/$', views.ItensContaAPagar.as_view(), name='itens_conta'),
    url(r'^finalizeconta/(?P<pk>\d+)/$', views.ConcluirConta.as_view(), name='concluir_conta'),
    url(r'^cadastrofornecedor/$', views.CadastroFornecedor.as_view(), name='criar_fornecedor'),
    url(r'^listafornecedor/$', list.ListView.as_view(model=Fornecedor), name='lista_fornecedor'),
    url(r'^editafornecedor/(?P<pk>\d+)/$', views.EditarFornecedor.as_view(), name='edita_fornecedor'),
    url(r'^deletafornecedor/(?P<pk>\d+)/$', views.DeletarFornecedor.as_view(), name='deleta_fornecedor'),
    url(r'^json/(?P<tipo>\w{0,50})/$', views.json, name='json'),
    url(r'^teste/', views.postteste.as_view(), name='postteste'),
    #url(r'^cliente/(?P<pk>\d+)/$', detail.DetailView.as_view(model=Cliente))
)
