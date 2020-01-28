from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import math
from django import forms
def validatingPhoneNo_validator (phoneNo):
    #digits = (int)(math.log10(phoneNo))
    #n = (phoneNo / pow(10, digits))
    n = str(phoneNo)
    if( len(n) !=10 ):
        raise ValidationError( _('Sorry, the phone number is not correct.') )
    return n

def confirmPhoneNo_validator (userPhoneNo):

    def __init__(self, userPhoneNo):
        v_userPhoneNo = self.all_clean_data
        userPhoneNo = userPhoneNo

    def __call__(self):
        if userPhoneNo != v_userPhoneNo:
            raise ValidationError(_('The Numbers have to match'))

def validatingPositiveWaitTime(waitTime):

    if waitTime < 0:
        raise ValidationError(_('Wait Time Cannot Be Less Than 0 MIN')) 
