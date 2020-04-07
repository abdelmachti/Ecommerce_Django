from django import forms
from django.contrib.auth import get_user_model



class ContactForm(forms.Form):
    fullname = forms.CharField( 
        widget=forms.TextInput(
            attrs={"class":"form-control", 
            "id":"form_full_name",
            "placeholder": "Your full name"
            }
            )
            )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class":"form-control",
            "placeholder":"Your Email"
            
            }))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class":"form-control",
            "placeholder":"Your Content"
            }
        )
    )


    def clean_email(self):
        email= self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email is not gmail")
        return email

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
