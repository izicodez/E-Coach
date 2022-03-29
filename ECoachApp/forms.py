
from django import forms
from ECoachApp.models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item","completed"]