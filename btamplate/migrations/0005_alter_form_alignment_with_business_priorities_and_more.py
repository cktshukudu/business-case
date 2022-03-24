# Generated by Django 4.0.2 on 2022-03-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btamplate', '0004_alter_form_business_case_proposal_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Alignment_with_Business_Priorities',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Approximate_costs_of_the_Project',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Business_case_proposal_date',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Estimate_Benefits_Financial_or_Non_Financial',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Estimated_completion_Date',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Impacted_Business_Function_or_Area',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Indicative_Risk_Level_of_the_Project',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Location_of_Project_Implementation',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Need_for_the_project',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Overall_Project_Timeframe',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Project_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Proposed_Solution_or_Methodology',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='Proposed_Start_Date',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='external_stakeholder',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='internal_stakeholder',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='manager',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='sponsor',
            field=models.CharField(max_length=300),
        ),
    ]