from django import forms
from .models import PigEntry
from django.contrib.admin import widgets


class PigEntryForm(forms.ModelForm):
    """
    Simple model form that contains input fields for the entry date and number of pigs entered
    Shown on pig entry page
    """
    class Meta:
        model = PigEntry
        fields = ('entry_date', 'number_of_pigs')

    def __init__(self, *args, **kwargs):
        super(PigEntryForm, self).__init__(*args, **kwargs)
        self.fields['entry_date'].widget = forms.DateInput(
            attrs={'class': 'dateInput',}
        )
       # self.fields['entry_date'].disabled = True
        self.fields['number_of_pigs'].label = "# of pigs"
        self.fields['number_of_pigs'].required = False
    
