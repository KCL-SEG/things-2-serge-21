"""Forms of the project."""
from django import forms
from things import models

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = models.Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea,
            'quantity': forms.NumberInput
            }
