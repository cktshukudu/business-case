from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewList



def index(response):
    return render(response, "btamplate/base.html", {})

def main(response):
    return render(response, "btamplate/main.html", {})




def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        # return HttpResponseRedirect('update/')
             
    else:
        form = CreateNewList()
    return render(response, "btamplate/create.html", {"form":form})