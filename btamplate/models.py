from django.db import models
from datetime import date




class Form(models.Model):
    company_logo = models.ImageField(upload_to='company_logos')
    Project_name = models.CharField(max_length=300)
    Business_case_proposal_date = models.CharField(max_length=300)
    sponsor = models.CharField(max_length=300)
    manager = models.CharField(max_length=300)
    internal_stakeholder = models.CharField(max_length=300)
    external_stakeholder = models.CharField(max_length=300)
    Need_for_the_project = models.CharField(max_length=300)
    Alignment_with_Business_Priorities = models.CharField(max_length=300)
    Proposed_Solution_or_Methodology = models.CharField(max_length=300)
    Impacted_Business_Function_or_Area = models.CharField(max_length=300)
    Indicative_Risk_Level_of_the_Project = models.CharField(max_length=300)
    Proposed_Start_Date =  models.CharField(max_length=300)
    Overall_Project_Timeframe = models.CharField(max_length=300)
    Estimated_completion_Date =  models.CharField(max_length=300)
    Location_of_Project_Implementation = models.CharField(max_length=300)
    Approximate_costs_of_the_Project = models.CharField(max_length=300)
    Estimate_Benefits_Financial_or_Non_Financial = models.CharField(max_length=300)
    Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial = models.CharField(max_length=300)
    def __str__(self):
        return self.Project_name
