from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length= 100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    sold = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.brand