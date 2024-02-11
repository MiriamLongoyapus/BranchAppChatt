from django import forms
from .models import CustomerMessage

class CusomerMessageUploadForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = '__all__'