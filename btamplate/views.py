from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewList
from .forms import RegisterForm
from .forms import LoginForm

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass 
    else: 
        form = RegisterForm()
    return render(request, 'btamplate/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass 
    else: 
        form = LoginForm()
    return render(request, 'btamplate/login.html', {'form': form})



def index(response):
    return render(response, "btamplate/base.html", {})

def main(response):
    return render(response, "btamplate/main.html", {})

def createTemplate(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        # return HttpResponseRedirect('update/')
             
    else:
        form = CreateNewList()
    return render(response, "btamplate/createTemplate.html", {"form":form})

    