from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label=False, widget=forms.TextInput(attrs={'cols': 30, 'rows': 60, 'placeholder': 'your sentence'},),
)