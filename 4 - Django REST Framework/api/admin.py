from django.contrib import admin
from api.models import Order, OrderItem, User, Product

class OrderAdminInline(admin.TabularInline): # Inlines são usados para exibir e editar objetos relacionados diretamente na página de administração do modelo pai. O TabularInline exibe os objetos relacionados em uma tabela, enquanto o StackedInline os exibe em um formato empilhado.
    model = OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderAdminInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(User)
admin.site.register(Product)