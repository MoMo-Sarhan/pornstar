from django import forms
from .models import Pornstar

class  PornstarForm(forms.ModelForm):
    
    class Meta:
        model = Pornstar
        fields = '__all__'
