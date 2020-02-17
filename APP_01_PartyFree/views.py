from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .import forms
from .tasks import sleepy
#twilio

# Create your views here.
def index_new(request):
    return render(request,'PartyFree/index_new.html')

def index(request):
    form = forms.UserForm()

    if request.method=='POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print( "Validation Sccess" )
            print(form.cleaned_data['userPhoneNo'])
            print(form.cleaned_data['waitTime'])
            sleepy.delay(form.cleaned_data['waitTime'],form.cleaned_data['userPhoneNo'])
            messages.success(request, 'Your call has been requested successfully.')
            return redirect('APP_01_PartyFree:partyfree-index')

    return render(request,'PartyFree/index.html',{'form':form})
