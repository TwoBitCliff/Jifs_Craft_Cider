from django.db import models
from checkout.models import Order

# Create your models here.

STATUS = (
    (0, "resolved"),
    (1, "unresolved")
)


class Refund(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    reason = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.order_number
