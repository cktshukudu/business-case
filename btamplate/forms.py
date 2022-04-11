from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Formi
from django.forms import ModelForm

class updateTemplate(forms.ModelForm):
    class Meta:
        model = Formi
        fields = ['pro_date', 'name','role','logo','summary','project','limitations','approach','benefits',
        'opportunities','nobel','threat','financial','risk']
 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        def save(self, commit=True):
            user = super(UserRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
class createForm(forms.Form):
    class Meta:
        model = Formi
        fields = ['pro_date','name','role','logo','summary','project','limitations','approach','benefits',
        'opportunities','nobel','threat','financial','risk']

