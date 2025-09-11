from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='phones')
    price=models.DecimalField(max_digits=12,decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


