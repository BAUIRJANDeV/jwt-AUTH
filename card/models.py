from django.db import models


from conf import settings
from products.models import Phone


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.phone.price

    def __str__(self):
        return f"{self.user.username} - {self.phone.name} ({self.quantity})"

# Create your models here.
