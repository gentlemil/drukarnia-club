from django import forms
from .models import Product, TypeOfProduct

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=250, label='', widget=forms.TextInput(attrs={'placeholder': 'amundsen', 'class':'form-control'}))
    prize = forms.CharField(max_length=250, label='', widget=forms.TextInput(attrs={'placeholder': '8/10, 12, 80', 'class':'form-control'}))
    types = forms.ModelChoiceField(queryset=TypeOfProduct.objects.all(), label='', widget=forms.Select(attrs={'placeholder': 'wybierz', 'class':'form-control'}))
    description = forms.CharField(max_length=250, label='', widget=forms.TextInput(attrs={'placeholder': 'cierpki, ostry w zapachu, delikatny w smaku', 'class':'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'prize', 'types', 'description']

# class TypeOfProductForm(forms.ModelForm):
#     name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'KATEGORIA'}))
#     amount = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': "ILOŚĆ (podaj w 'ml')"})

#     class Meta:
#         model = TypeOfProduct
#         fields = ['name', 'amount']
