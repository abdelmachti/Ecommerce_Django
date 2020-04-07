from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

User =get_user_model()
class RegisterForm(forms.Form):
    firstname = forms.CharField()
    secondname = forms.CharField()
    adresse = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword =forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs= User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken!!")
        return username
    
    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs= User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken!!")
        return email
        
    def clean(self):
        data= self.cleaned_data
        password= data.get("password")
        confirmpassword=data.get("repassword")
        if confirmpassword != password:
            raise forms.ValidationError("Password must  match!!")
        return data