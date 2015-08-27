from django import forms

from .pet import petnames


class PetName(forms.ModelForm):

    pet_name = forms.TextInput(
        initial='miniBug',
        required=True,
        label='What is the name of your favorite pet?',
    )



