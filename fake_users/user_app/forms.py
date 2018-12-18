from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(widget=forms.EmailInput)
    verify_email = forms.EmailField(widget=forms.EmailInput)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vemail = cleaned_data['verify_email']

        # checks to make sure the emails match
        if email != vemail:
            raise forms.ValidationError("emails do not match, please verify")

        # check to make sure there is at least one number in the emails
        if any(char.isdigit() for char in email) != True:
            raise forms.ValidationError("email must contain at least one number")
