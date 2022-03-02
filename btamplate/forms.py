from django import forms
from django.forms.widgets import NumberInput

class RegisterForm(forms.Form):
    company_email_address = forms.EmailField()
    phone_number = forms.CharField(label='Phone')
    company_number = forms.CharField()
    office_adress = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    company_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class CreateNewList(forms.Form):
    Project_name = forms.CharField(max_length=200)
    Business_case_proposal_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    sponsor = forms.CharField(widget=forms.TextInput(attrs={'title':"id_sponsor","id":"id_sponsor",'size':'10','maxlength':'200'} ))
    manager = forms.CharField(widget=forms.TextInput(attrs={'title':"id_manager","id":"id_manager",'size':'60','maxlength':'200'} ))
    internal_stakeholder = forms.CharField(widget=forms.TextInput(attrs={'title':"id_internal","id":"id_internal",'size':'60','maxlength':'200'} ))
    external_stakeholder = forms.CharField(widget=forms.TextInput(attrs={'title':"id_external","id":"id_external",'size':'60','maxlength':'200'} ))
    Need_for_the_project = forms.CharField(widget=forms.TextInput(attrs={'title':"id_pro","id":"id_pro",'size':'60','maxlength':'200'} ))
    Alignment_with_Business_Priorities = forms.CharField(widget=forms.TextInput(attrs={'title':"id_alignment","id":"id_alignment",'size':'60','maxlength':'200'} ))
    Proposed_Solution_or_Methodology = forms.CharField(widget=forms.TextInput(attrs={'title':"id_solution","id":"id_solution",'size':'60','maxlength':'200'} ))
    Impacted_Business_Function_or_Area = forms.CharField(widget=forms.TextInput(attrs={'title':"id_area","id":"id_area",'size':'60','maxlength':'200'} ))
    Indicative_Risk_Level_of_the_Project = forms.CharField(widget=forms.TextInput(attrs={'title':"id_risk","id":"id_risk",'size':'60','maxlength':'200'} ))
    Proposed_Start_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Overall_Project_Timeframe = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Estimated_completion_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Location_of_Project_Implementation = forms.CharField(widget=forms.TextInput(attrs={'title':"id_location","id":"id_location",'size':'60','maxlength':'200'} ))
    Approximate_costs_of_the_Project = forms.CharField(widget=forms.TextInput(attrs={'title':"id_costs","id":"id_costs",'size':'60','maxlength':'200'} ))
    estimate = forms.CharField(label="Estimate Benefits(Financial or Non-Financial):", max_length=200)
    impact = forms.CharField(label="Impact/Risks of doing nothing(Financial or Non-Financial):", max_length=200)
