from django import forms
from .models import WorkWithUs


class WorkWithUsForm(forms.ModelForm):
    class Meta:
        model = WorkWithUs
        fields = ('name', 'email', 'message')
