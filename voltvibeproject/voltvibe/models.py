from django.db import models

# used to define databases, tables 
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    #is_seller = models.BooleanField(default=False)  # To differentiate between buyers and sellers
    password = models.CharField(max_length=128)  # Storing hashed passwords
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='pending')  # Status of the order

    def __str__(self):
        return f"{self.pk} {self.first_name} {self.last_name}"  # Return full name

# Orders model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    item = models.CharField(max_length=100, default='your_default_value')
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the order is created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the order
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='pending')  # Status of the order
    shipping_address = models.TextField(blank=True, null=True)  # Shipping address for the order

    def __str__(self):
        return f"Order {self.id} by {self.user}"  # Return a string representation of the order

    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Automatically incrementing ID
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField(blank=True, null=True)  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock_quantity = models.PositiveIntegerField(default=0)  # Available stock quantity
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the seller (User)
    
    def __str__(self):
        return self.name  # Return the product name

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)  # Automatically incrementing ID
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Link to the Orders model
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    transaction_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the transaction occurs
    status = models.CharField(max_length=20, choices=[
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ], default='pending')  # Status of the transaction

    def __str__(self):
        return f"Transaction {self.transaction_id} for Order {self.order.id}"  # Return a string representation of the transaction
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

