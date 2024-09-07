from django import forms
from .models import Zakatdetails,Madrasadetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','last_name','email','username', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class madrasaregisteration(forms.ModelForm):
    class Meta:
        model = Madrasadetails
        fields = ['madrasaname','address','phone']
     
class zakatentry(forms.ModelForm):
    class Meta:
        model = Zakatdetails 
       
        fields = ['madrasa_name', 'zakat_date','zakat_amount','slip_no']
        
        widgets = {
            'zakat_date': forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'DD-MM-YYYY'})
        }
     