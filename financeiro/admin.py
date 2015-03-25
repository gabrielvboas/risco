from django.contrib import admin
from financeiro.models import Relatorio, ContaAPagar, ContaAReceber

# Register your models here.
admin.site.register(Relatorio)
admin.site.register(ContaAPagar)
admin.site.register(ContaAReceber)

