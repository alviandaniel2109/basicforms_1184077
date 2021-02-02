from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp_1184077/index.html')

def form_name_view(request):
    form = forms.ForName()

    if request.method == 'POST':
        form= forms.ForName(request.POST)

        if form.is_valid():
            #do something
            print("validation success")
            print("First Name :"+form.cleaned_data['firstname'])
            print("Last Name :"+form.cleaned_data['lastname'])
            print("EMAIL :"+form.cleaned_data['email'])
            print("Gender :"+form.cleaned_data['gender'])
            print("TEXT :"+form.cleaned_data['text'])

    return render(request,'basicapp_1184077/form_page.html', {'form':form})