from django import forms
from .models import Product, TypeOfProduct

# --- formularz do edycji pozycji w menu
class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Produkt'}))
    prize = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Cena (np. 8/10, 12)'}))
    types = forms.ModelChoiceField(label="Rodzaj:", queryset=TypeOfProduct.objects.all(), widget=forms.Select())
    description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Rodzaj'}))


    class Meta:
        model = Product
        fields = ['name', 'prize', 'types']

# class TypeOfProductForm(forms.ModelForm):
#     name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'KATEGORIA'}))
#     amount = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': "ILOŚĆ (podaj w 'ml')"})

#     class Meta:
#         model = TypeOfProduct
#         fields = ['name', 'amount']
