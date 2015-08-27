from django.shortcuts import render, render_to_response, HttpResponseRedirect

from .models import Pizza

from .forms import PizzaCreateForm


def pizza(request):
    if request.method == 'POST':
        form = PizzaCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../view_pizza')

    else:
        form = PizzaCreateForm()

    return render(request, 'pizza.html', {'form': form, 'button_name': 'Create!'})


def viewPizza(request):
    pizza_list = Pizza.objects.all()

    return render_to_response(
        'view_pizza.html',
        context={
            'pizzas': pizza_list
        }
    )




