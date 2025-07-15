from django import forms

from store.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        widgets = {
            'value': forms.RadioSelect(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])
        }