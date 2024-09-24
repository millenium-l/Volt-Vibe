from django.contrib import admin
from .models import User, Order, Product, Transaction


# Register the User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birth_date', 'phone_number', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('birth_date',)

# Register your models here.
admin.site.register(User, UserAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'shipping_address', 'status', 'total_amount')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')  # Use double underscore to access related fields
    list_filter = ('shipping_address',)

admin.site.register(Order, OrdersAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')
    
admin.site.register(Product, ProductAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'status')
    search_fields = ('status',)

admin.site.register(Transaction, TransactionAdmin)
