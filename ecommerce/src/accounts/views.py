from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm
# Create your views here.


def login_page(request):
    form = LoginForm(request.POST or None)
    context={
        "title":"Login",
        "form":form
    }
    print("User logged in")
    #print(request.user.is_authenticated)
    next = request.GET.get('next')
    next_post= request.POST.get('next')
    redirect_path = next or next_post or None
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user= authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            #Redirect to a success page.
            #context ['form'] = LoginForm()
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            #Return an invalid login erro message
            print("invalid login")
    
    return render(request, "accounts/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context={
        "title":"Register",
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        email=form.cleaned_data.get("email")
        new_user= User.objects.create_user(username,email,password)
        print(new_user)
    return render(request, "accounts/register.html", context)