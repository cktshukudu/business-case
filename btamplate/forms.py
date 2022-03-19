from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Form



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
class createForm(forms.Form):
    class Meta:
        model = Form
        fields = ['company_logo','Project_name','Business_case_proposal_date','sponsor','manager','internal_stakeholder',
            'external_stakeholder','Need_for_the_project','Alignment_with_Business_Priorities','Proposed_Solution_or_Methodology',
            'Impacted_Business_Function_or_Area','Indicative_Risk_Level_of_the_Project','Proposed_Start_Date','Overall_Project_Timeframe',
            'Estimated_completion_Date','Location_of_Project_Implementation','Approximate_costs_of_the_Project','Estimate_Benefits_Financial_or_Non_Financial',
            'Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial']
