from django.contrib import admin
from financeiro.models import Relatorio, Conta, Cliente

# Register your models here.
admin.site.register(Relatorio)
admin.site.register(Conta)
admin.site.register(Cliente)

