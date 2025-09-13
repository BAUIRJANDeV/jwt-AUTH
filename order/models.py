from django.db import models
from conf import settings
from products.models import Phone

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.user.username}"

    def total_price(self):
        return sum([item.total_price() for item in self.items.all()])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.phone.price * self.quantity

    def __str__(self):
        return f"{self.phone.name} ({self.quantity} dona)"

# Create your models here.
