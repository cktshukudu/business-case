from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import createForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            Project_name = form.cleaned_data['Project_name']
            Business_case_proposal_date  = form.cleaned_data['Business_case_proposal_date ']
            sponsor = form.cleaned_data['sponsor']
            manager = form.cleaned_data['manager']
            internal_stakeholder  = form.cleaned_data['internal_stakeholder ']
            external_stakeholder = form.cleaned_data['external_stakeholder']
            Need_for_the_project = form.cleaned_data['Need_for_the_project']
            Alignment_with_Business_Priorities = form.cleaned_data['Alignment_with_Business_Priorities']
            Proposed_Solution_or_Methodology  = form.cleaned_data['Proposed_Solution_or_Methodology ']
            Impacted_Business_Function_or_Area = form.cleaned_data['Impacted_Business_Function_or_Area']
            Indicative_Risk_Level_of_the_Project = form.cleaned_data['Indicative_Risk_Level_of_the_Project']
            Proposed_Start_Date = form.cleaned_data['Proposed_Start_Date']
            Overall_Project_Timeframe = form.cleaned_data['Overall_Project_Timeframe']
            Estimated_completion_Date = form.cleaned_data['Estimated_completion_Date']
            Location_of_Project_Implementation = form.cleaned_data['Location_of_Project_Implementation']
            Approximate_costs_of_the_Project = form.cleaned_data['Approximate_costs_of_the_Project']
            estimate = form.cleaned_data[' estimate']
            impact = form.cleaned_data['impact']
            return redirect('createTemplate')  
    else: 
        form = createForm()
    return render(request, 'btamplate/update.html', {'form': form})

def index(response):
    return render(response, "btamplate/base.html", {})

def main(response):
    return render(response, "btamplate/main.html", {})

def update(response):
    return render(response, "btamplate/update.html", {})

def about_us(response):
    return render(response, "btamplate/about_us.html", {})


    