from django import forms
from .models import PigEntry
from django.contrib.admin import widgets

class PigEntryForm(forms.ModelForm):
    class Meta:
        model = PigEntry
        fields = ('entry_date', 'number_of_pigs', 'room_number')
       