from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    def __str__(self):
        
        return self.name
    
class Customer(models.Model):
    # GENDER_CHOICES = (
    #     ('MALE','male')
    #     ('FEMALE','female')
    # )
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    address = models.TextField()
    gender = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING','pending'),
        ('COMPLETED','completed'),
        ('CANCELED','cancelled'),
    )    
    
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits = 10, decimal_places = 4)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'pending')
    
    def __str__(self):
        
        return f"Your Order {self.id} - {self.customer}"
