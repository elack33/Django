from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


from .forms import MailingListForm, SetMailingLists


def add_email(request):

    if request.method == 'POST':
        form = MailingListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mailinglist/thanks')

    else:
        form = MailingListForm()

    return render_to_response(
        'add_email.html',
        {'form': form},
        RequestContext(request),
    )


def thanks(request):
    return render_to_response(
        'thanks.html',
    )

def thankyou(request):
    return render_to_response(
        'thankyou.html',
    )

def myform(request):

    if request.method == 'POST':
        form = SetMailingLists(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('mailinglist/thankyou')
    else:
        form = SetMailingLists()

    return render_to_response(
        'myform.html',
        {'form': form},
        RequestContext(request)
    )


