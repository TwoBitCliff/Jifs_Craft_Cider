from django import forms
from .models import Refund

# https://www.youtube.com/watch?v=PJkV76KTZqk


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ('order_number', 'full_name', 'email', 'reason')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'order_number': 'Please enter the first 5 digits of the order number',
            'full_name': 'Full Name',
            'email': 'Email',
            'reason': 'Reason for refund'
        }

        self.fields['order_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-blue rounded-0'
            self.fields[field].label = False
