from ctypes import alignment
from multiprocessing import Manager
from tabnanny import check
from unicodedata import name
from django import forms
from django import forms



class CreateNewList(forms.Form):
    name = forms.CharField(label="Project Name:", max_length=200)
    pro_date= forms.DateField(label='Business Case Proposal Date', widget=forms.SelectDateWidget)
    
  


    