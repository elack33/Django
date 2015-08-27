from django import forms
from django.contrib.auth.models import User


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password2'] = forms.CharField(
            widget=forms.PasswordInput(),
            label='Password Confirm',
        )