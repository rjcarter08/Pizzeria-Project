from django import forms 
from .models import Pizza, Topping

class PizzaForm(forms.ModelForm): 
    class Meta: 
        model = Pizza 
        fields = ['name']
        labels = {'text':''} 

class ToppingForm(forms.ModelForm):
    class Meta: 
        model = Topping
        fields = ['pizza','name']
        labels = {'text':''} 
        widgets = {'text':forms.Textarea(attrs={'cols':80})}