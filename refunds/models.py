from django.db import models

# Create your models here.

STATUS = (
    (0, "unresolved"),
    (1, "resolved")
)


class Refund(models.Model):
    order_number = models.CharField(max_length=5, null=False, blank=False,
                                    default='00000')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    reason = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.email
