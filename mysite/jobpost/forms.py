from django import forms
from .models import JobPost
from django.contrib.auth.models import User

from .models import Roles


class NewJobPost(forms.Form):

    title = forms.CharField(
        label="Job title:",
        max_length=255,
    )

    description = forms.CharField(
        widget=forms.Textarea,
        label="description",
    )

    def save(self):
        title = self.cleaned_data['title']
        descrip = self.cleaned_data['description']

        JobPost.objects.create(
            title=title,
            job_description=descrip
        )


class DeleteListForm(forms.Form):
    jobs_list = forms.ChoiceField(
        label='List to delete',
    )

    def __init__(self, *args, **kwargs):
        super(DeleteListForm, self).__init__(*args, **kwargs)
        choices = [
            (jobs.id, jobs.title) for jobs in JobPost.objects.all()
        ]
        self.fields['jobs_list'].choices = choices

    def save(self):
        jobs_list_id = self.cleaned_data['jobs_list']
        jobs_list = JobPost.objects.get(id=jobs_list_id)
        jobs_list.delete()


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['role'] = forms.ChoiceField(
            choices=Roles.ROLES_CHOICES,
        )

    def save(self):
        new_user = super(CreateUserForm, self).save()

        roles = self.cleaned_data['role']
        Roles.objects.create(
            user=new_user,
            roles=roles,
        )

        pw = self.cleaned_data['password']
        new_user.set_password(pw)
        new_user.save()
        return new_user

