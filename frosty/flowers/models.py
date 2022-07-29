from django.db import models
from django.contrib.auth.models import AbstractUser


FLOWER_COLORS = [
    ('RD', 'Red'),
    ('BL', 'Blue'),
    ('WT', 'White'),
    ('GR', 'Greed'),
    ('PP', 'Purple'),
]

USER_ROLES = (
    ('SL', 'Seller'),
    ('BY', 'Buyer'),
)


class User(AbstractUser):
    role = models.CharField(choices=USER_ROLES, max_length=2)


class Flower(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    color = models.CharField(choices=FLOWER_COLORS, max_length=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Lot(models.Model):
    item = models.ForeignKey(Flower, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item}"


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_feedback')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_feedback', null=True, blank=True)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='lot_feedback', null=True, blank=True)
    text = models.TextField()
