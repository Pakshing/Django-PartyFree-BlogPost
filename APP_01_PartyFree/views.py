from django.shortcuts import render
from django.http import HttpResponse
from .import forms
from .tasks import sleepy
#twilio

# Create your views here.

def index(request):
    form = forms.UserForm()

    if request.method=='POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print( "Validation Sccess" )
            print(form.cleaned_data['userPhoneNo'])
            print(form.cleaned_data['waitTime'])
            sleepy.delay(form.cleaned_data['waitTime'],form.cleaned_data['userPhoneNo'])
            return render(request,'PartyFree/finish_page.html')
    return render(request,'PartyFree/index.html',{'form':form})
