from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Form
from django.utils import timezone



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
       company_logo = request.POST.get("company_logo", "")
       Project_name = request.POST.get("Project_name", "")
       Business_case_proposal_date = request.POST.get("Business_case_proposal_date")
       sponsor = request.POST.get("sponsor", "")
       manager = request.POST.get("manager", "")
       internal_stakeholder = request.POST.get("internal_stakeholder", "")
       external_stakeholder = request.POST.get("external_stakeholder", "")
       Need_for_the_project = request.POST.get("Need_for_the_project", "")
       Alignment_with_Business_Priorities = request.POST.get("Alignment_with_Business_Priorities", "")
       Proposed_Solution_or_Methodology = request.POST.get("Proposed_Solution_or_Methodology", "")
       Impacted_Business_Function_or_Area = request.POST.get("Impacted_Business_Function_or_Area", "")
       Indicative_Risk_Level_of_the_Project = request.POST.get("Indicative_Risk_Level_of_the_Project", "")
       Proposed_Start_Date = request.POST.get("Proposed_Start_Date")
       Overall_Project_Timeframe = request.POST.get("Overall_Project_Timeframe")
       Estimated_completion_Date = request.POST.get("Estimated_completion_Date")
       Approximate_costs_of_the_Project = request.POST.get("Approximate_costs_of_the_Project", "")
       Estimate_Benefits_Financial_or_Non_Financial = request.POST.get("Estimate_Benefits_Financial_or_Non_Financial", "")
       Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial = request.POST.get("Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial", "")

    form = Form(company_logo=company_logo,Project_name=Project_name,
    Business_case_proposal_date=Business_case_proposal_date,
       sponsor=sponsor,manager=manager,internal_stakeholder=internal_stakeholder,external_stakeholder=external_stakeholder,
       Need_for_the_project=Need_for_the_project,Alignment_with_Business_Priorities=Alignment_with_Business_Priorities,
       Proposed_Solution_or_Methodology=Proposed_Solution_or_Methodology,Impacted_Business_Function_or_Area=Impacted_Business_Function_or_Area,
    Indicative_Risk_Level_of_the_Project=Indicative_Risk_Level_of_the_Project,
    Proposed_Start_Date=Proposed_Start_Date,
       Overall_Project_Timeframe=Overall_Project_Timeframe,Estimated_completion_Date=Estimated_completion_Date,
    Approximate_costs_of_the_Project=Approximate_costs_of_the_Project,
       Estimate_Benefits_Financial_or_Non_Financial=Estimate_Benefits_Financial_or_Non_Financial,Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial=Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial
       )
    form.save()

    return render(request, "btamplate/createTemplate.html")

def index(request):
    return render(request, "btamplate/base.html", {})

def main(request):
    return render(request, "btamplate/main.html", {})

def update(request, id):
    user_form = Form.objects.get(pk=id)
    return render(request, "btamplate/update.html",{'user_form':user_form})

def about_us(request):
    return render(request, "btamplate/about_us.html", {})


    