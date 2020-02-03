from django import forms
from django.core import validators
from .validators import validatingPhoneNo_validator,confirmPhoneNo_validator, validatingPositiveWaitTime


class UserForm(forms.Form):

    userPhoneNo = forms.CharField(validators=[validatingPhoneNo_validator],widget=forms.TextInput(attrs={'class' : 'form-control'}))
    v_userPhoneNo = forms.CharField(label='Enter your phone number again.',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    waitTime = forms.IntegerField(label='min(s): must be positive integer',validators=[validatingPositiveWaitTime],widget=forms.TextInput(attrs={'class' : 'form-control'}))

    def clean_v_userPhoneNo(self):
        passed_number = self.cleaned_data.get("userPhoneNo")
        passed_number2 = self.cleaned_data.get('v_userPhoneNo')
        if passed_number != passed_number2:
            raise forms.ValidationError('Phone Numbers must be matched')
        else:
            return passed_number2
