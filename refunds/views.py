from django.shortcuts import render, redirect, reverse
from .models import Refund
from .forms import RefundForm
from django.contrib import messages


def RefundList(request):
    """ A view to display ongoing refund requests posts """

    refunds = Refund.objects.all()

    context = {
        'refunds': refunds,
    }

    return render(request, 'refunds/refund.html', context)


def RequestRefund(request):
    """  Adds a post to the blog  """
    if request.method == 'POST':
        form = RefundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Refund submitted!')
            return redirect(reverse('refunds'))
        else:
            messages.error(request, 'Failed to submit refund. Please ensure the form is valid.')
    else:
        form = RefundForm()
    template = 'refunds/refund-form.html'
    context = {
        'form': form
    }

    return render(request, template, context)