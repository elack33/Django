from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import PurchaseForm, AddGift
from .models import Wedding

def purchase(request, wedding_id):
    wedding = get_object_or_404(Wedding, pk=wedding_id)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, wedding=wedding)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thanks'))

    else:
        form = PurchaseForm(wedding=wedding)

    return render(
        request,
        'purchase.html',
        {
            'form': form,
            'wedding': wedding,
        }
    )


def add_gift(request):

    if request.method == 'POST':
        form = AddGift(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = AddGift()

    return render(
        request,
        'add_gift.html',
        {
            'form': form,
        }
    )