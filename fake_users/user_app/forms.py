from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(widget=forms.EmailInput)
    text = forms.CharField(widget=forms.Textarea)
