from django.conf.urls import patterns, include, url
from financeiro import views


urlpatterns = patterns('',
    url(r'^cadastroconta/', views.CadastroConta.as_view(), name='CadastroConta'),
)

