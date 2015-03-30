from django.conf.urls import patterns, include, url
from financeiro import views


urlpatterns = patterns('',
    url(r'^$', views.brunao, name='brunao'),
    url(r'^CadastroConta/', views.CadastroConta.as_view(), name='CadastroConta'),
)

