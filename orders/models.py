from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Order(models.Model):
    statuses = [(1, "Created"), (2, "In process"), (3, "Sended"), (4, "Completed")]

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.IntegerField(choices=statuses)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.client.username} {self.status}"


class Book(models.Model):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    description = HTMLField()
    pages = models.IntegerField()
    available = models.IntegerField()
    price = models.FloatField()
    release = models.DateField()

    def __str__(self) -> str:
        return self.title


class CartBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()


# class MyUser(User):
#     shef = models.BooleanField()
