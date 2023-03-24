from django import forms
from mirai.models import Employee
from mirai.models import Company


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

