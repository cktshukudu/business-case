
from ctypes import alignment
from multiprocessing import Manager
from unicodedata import name
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
        if form.is_valid():
             name = form.cleaned_data['name']
             name.save()
             pro_date = form.cleaned_data['pro_date']
             pro_date.save()
             sponsor = form.cleaned_data['sponsor']
             sponsor.save()
             Manager = form.cleaned_data['Manager']
             Manager.save()
             istakeholder = form.cleaned_data['istakeholder']
             istakeholder.save()
             estakeholder = form.cleaned_data['estakeholder']
             estakeholder.save()
             Project = form.cleaned_data['Project']
             Project.save()
             alignment = form.cleaned_data['aligment']
             alignment.save()
             solution = form.cleaned_data['solution']
             solution.save()
             area = form.cleaned_data['area']
             area.save()
             start = form.cleaned_data['risk']
             start.save()
             Overall = form.cleaned_data['Overall']
             Overall.save()
             completion = form.cleaned_data['completion']
             completion.save()
             Location = form.cleaned_data['Location']
             Location.save()
             costs = form.cleaned_data['costs']
             costs.save()
             Estimate = form.cleaned_data['Estimate']
             Estimate.save()
             Impact = form.cleaned_data['Impact']
             Impact.save()

             return HttpResponseRedirect('/thanks/')
             
    else:
        form = CreateNewList()
    return render(response, "btamplate/create.html", {"form":form})