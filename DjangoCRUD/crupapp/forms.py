from django import forms
from crupapp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets={
            'uname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'upassword': forms.TextInput(attrs={'class': 'form-control'})
        }