from django.contrib import admin
from financeiro.models import *

# Register your models here.
admin.site.register(Relatorio)
admin.site.register(ContaAPagar)
admin.site.register(Conta)
admin.site.register(ProductRequest)
admin.site.register(StockRequest)
admin.site.register(CheckoutPayment)
admin.site.register(CheckInConfirmation)
admin.site.register(Reservation)
admin.site.register(Fornecedor)

