from django import forms
from django.core import validators


def check_for_z(value): 
    if value[0].lower() != 'z':
        raise forms.ValidationError("Nama Harus Dimulai Dari Huruf Z")

def check_for_k(value):
    if value[-1].lower() != 'k':
        raise forms.ValidationError("Nickname Harus diakhiri Huruf K ")

class ForName(forms.Form):
    firstname = forms.CharField(validators=[check_for_z])
    lastname = forms.CharField(validators=[check_for_k])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter you email again NPM')
    CHOICES = [('L', 'Laki-Laki'), ('P', 'Perempuan')]
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    text = forms.CharField(widget=forms.Textarea)


    #Method untuk menghaous isi form
    def clean(self):

        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        #melakukan validator harus sama
        if email != vmail:
            raise forms.ValidationError("MAKE SURE YOURE EMAILS MATCH")