# from django.db import models
# from .forms import CreateNewList
# from crispy_forms.layout import Submit
# from crispy_forms.helper import FormHelper


# class InfoCreateView(models.Model):
#     class Meta:
#         model = CreateNewList
#     fields = ('name', 'pro_date', 'sponsor', 'manager', 'internal_stakeholder',
#     'external_stakeholder','Need_for_the_project',' Alignment_with_Business_Priorities','Proposed_Solution_or_Methodology',
#      'Impacted_Business_Function_or_Area','Indicative_Risk_Level_of_the_Project','start_date','over_date','completion_date',
#      'Location_of_Project_Implementation','Approximate_costs_of_the_Project','estimate','impact' )
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'save'))

# from django.db import models
# from django.forms.widgets import SelectDateWidget

# class CreateNewList(models.Model):
#     name = models.CharField(max_length=200)
#     # Business_Case_Proposal_Date = models.DateField(SelectDateWidget)
#     sponsor = models.CharField(max_length=200)
#     manager = models.CharField(max_length=200)
#     internal_stakeholder = models.CharField(max_length=200)
#     external_stakeholder = models.CharField(max_length=200)
#     Need_for_the_project = models.CharField(max_length=200)
#     Alignment_with_Business_Priorities = models.CharField(max_length=200)
#     Proposed_Solution_or_Methodology = models.CharField(max_length=200)
#     Impacted_Business_Function_or_Area = models.CharField(max_length=200)
#     Indicative_Risk_Level_of_the_Project = models.CharField(max_length=200)
#     # Proposed_Start_Date = models.DateField(SelectDateWidget)
#     # Overall_Project_Timeframe = models.DateField(SelectDateWidget)
#     # Estimated_completion_Date = models.DateField(SelectDateWidget)
#     Location_of_Project_Implementation = models.CharField(max_length=200)
#     Approximate_costs_of_the_Project = models.CharField(max_length=200)
#     Estimate_Benefits = models.CharField(max_length=200)
#     Impact_OR_Risks_of_doing_nothing = models.CharField(max_length=200)
    