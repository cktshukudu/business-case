
from ctypes import alignment
from multiprocessing import Manager
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewList
from .forms import BasicForm

def crispy_signup(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass 
    else: 
        form = BasicForm()
    return render(request, 'crispy_signup.html', {'form': form})


def index(response):
    return render(response, "btamplate/base.html", {})

def main(response):
    return render(response, "btamplate/main.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
             name = form.cleaned_data['name']
             pro_date = form.cleaned_data['pro_date']
             sponsor = form.cleaned_data['sponsor']
             manager = form.cleaned_data['manager']
             
             internal_stakeholder = form.cleaned_data['internal_stakeholder']
             
             external_stakeholder= form.cleaned_data['external_stakeholder']
        
             Need_for_the_project = form.cleaned_data['Need_for_the_project']
             
             Alignment_with_Business_Priorities = form.cleaned_data[' Alignment_with_Business_Priorities']
            
             Proposed_Solution_or_Methodology = form.cleaned_data['Proposed_Solution_or_Methodology']
             
             Impacted_Business_Function_or_Area = form.cleaned_data['Impacted_Business_Function_or_Area']
             
             Indicative_Risk_Level_of_the_Project = form.cleaned_data['Indicative_Risk_Level_of_the_Project']
            
             start_date = form.cleaned_data['start_date']
            
             over_date = form.cleaned_data['over_date']
             completion_date = form.cleaned_data['completion_date']
             
             Location_of_Project_Implementation = form.cleaned_data[' Location_of_Project_Implementation']
             
             Approximate_costs_of_the_Project = form.cleaned_data['Approximate_costs_of_the_Project']
             
             estimate = form.cleaned_data['estimate']
             
             impact = form.cleaned_data['impact']
             

            #  return HttpResponseRedirect('create/')
             
    else:
        form = CreateNewList()
    return render(response, "btamplate/create.html", {"form":form})