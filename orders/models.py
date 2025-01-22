from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    status =models.CharField(
        max_length=20,
        choices=(
            ('Pending', 'Pending'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled'),
        ),
        default='Pending'
    )

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


