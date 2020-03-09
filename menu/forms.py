from django import forms
from .models import Product, TypeOfProduct

# --- formularz do edycji pozycji w menu
class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Podaj nazwe'}))
    prize = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Podaj cene'}))
    types = forms.ModelChoiceField(label="Rodzaj:", queryset=TypeOfProduct.objects.all(), widget=forms.Select())

    class Meta:
        model = Product
        fields = ['name', 'prize', 'types']
