from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import createForm


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'btamplate/signup.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'btamplate/createTemplate.html')

def createTemplate(request):
      if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            createForm.save()
            return redirect("update.html") 
        else: 
            form = createForm()
        return render(request, 'btamplate/createTemplate.html', {'form': form})


def index(request):
    return render(request, "btamplate/base.html", {})

def main(request):
    return render(request, "btamplate/main.html", {})

def update(request):
    return render(request, "btamplate/update.html")

def about_us(request):
    return render(request, "btamplate/about_us.html", {})


    