from django.test import TestCase

from . import forms


class TestCreateJobPostForm(TestCase):

    def setUp(self):
        self.data = {
            'title': 'Big Green Wheeling Machine',
            'job_description': 'Dodging shells, eating power ups and flying through turns!',
            'Roles': 'RO',
        }

    def test_creates_roles_field_at_init(self):
        form = forms.NewJobPost()
        self.assertIsNotNone(form.fields.get('Roles'))
