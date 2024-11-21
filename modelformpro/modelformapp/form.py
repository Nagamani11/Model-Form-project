from django import forms
from .models import EmpData

class EmpDataForm(forms.ModelForm):
    class Meta:
        model = EmpData
        fields = '__all__'
