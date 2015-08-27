from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'input'})
        self.fields['last_name'].widget.attrs.update({'class': 'input'})
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})

    def clean_username(self):
        data = self.cleaned_data['username']
        if len('username') < 6:
            raise forms.ValidationError("Username must be more than 6 characters.")
        return data
