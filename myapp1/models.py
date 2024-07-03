from django.db import models
import datetime
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO')
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)

    class Meta:
        verbose_name_plural = 'Client'

    def __str__(self):
        return self.first_name + self.last_name


class OrderItems(models.Model):
    items = models.ForeignKey(Item, related_name="order_items", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number_of_items = models.PositiveIntegerField()
    STATUS_CHOICES = [
        ('0', 'Cancelled order'),
        ('1', 'Placed Order'),
        ('2', 'Shipped Order'),
        ('3', 'Delivered Order')
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    last_updated = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.items.name


class Description(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    when_added = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.title
