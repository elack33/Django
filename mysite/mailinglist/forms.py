from django import forms

from .models import MailingList, Email


class MailingListForm(forms.Form):
    email_address = forms.EmailField(
        initial='reina@example.com',
        required=True,
        label='What\'s your addy?',
        help_text='if you enter your address we will spam you...',
    )

    def save(self):
        # get the value of `email_address` from the form
        email = self.cleaned_data['email_address']

        # use that value to create a new Email object in the db
        new_email = Email.objects.create(email_address=email)

        # find the list to add the email address to
        mylist = MailingList.objects.first()

        # add it!
        mylist.emails.add(new_email)

# def get_my_choices():
#         choices_list = MailingList.objects.all()
#         return choices_list

class SetMailingLists(forms.Form):

    # def __init__(self, *args, **kwargs):
    #     super(SetMailingLists, self).__init__(*args, **kwargs)
    #     self.fields['my_choice_field'] = forms.ChoiceField(
    #         choices=get_my_choices() )

    mailinglists = forms.MultipleChoiceField(
        label='Mailing lists',
    )

    def __init__(self, *args, **kwargs):
        super(SetMailingLists, self).__init__(*args, **kwargs)
        mailing_listchoices = []
        for mailinglist in MailingList.objects.iterator():
            mailing_listchoices.append((mailinglist.id, mailinglist.name))
        self.fields['mailinglists'].choices = mailing_listchoices



    email_address = forms.EmailField(
        initial='None@none.com',
        required=True,
        label='Enter your email address',

    )

    # mailing_list = forms.ModelMultipleChoiceField(queryset=MailingList.objects.values_list('name'),
    #                                               label="choice wisely")

    # mail_list = get_my_choices()

    def save(self):
        email = self.cleaned_detail['email_address']
        mailinglist_ids = self.cleaned_data['mailinglists']

        new_email, _ = Email.objects.create(email_address=email)
        for maillinglist_id in mailinglist_ids:
            mailinglist = MailingList.objects.get(id=mailinglist_id)
            mailinglist.emails.add(new_email)





