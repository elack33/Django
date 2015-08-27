from django import forms

from .models import Pizza


class PizzaCreateForm(forms.ModelForm):
    class Meta:
        model = Pizza
        exclude = []

