from django import forms
from .models import Refund

# https://www.youtube.com/watch?v=PJkV76KTZqk


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ('order_number', 'full_name', 'email', 'reason')
        