from django import forms
from django.core import validators
from .validators import validatingPhoneNo_validator,confirmPhoneNo_validator


class UserForm(forms.Form):

    userPhoneNo = forms.CharField(validators=[validatingPhoneNo_validator])
    v_userPhoneNo = forms.CharField(label='Enter your phone number again.')
    waitTime = forms.IntegerField()

    def clean_v_userPhoneNo(self):
        passed_number = self.cleaned_data.get("userPhoneNo")
        passed_number2 = self.cleaned_data.get('v_userPhoneNo')
        if passed_number != passed_number2:
            raise forms.ValidationError('Phone Numbers must be matched')
        else:
            return passed_number2
