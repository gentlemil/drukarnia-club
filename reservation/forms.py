from django import forms
from .models import Reservation, Bar

class ReservationForm(forms.ModelForm):

    name = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Jan Kowalski', 'class':'form-control'}))
    email = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'placeholder': 'jan@kowalski.com', 'class':'form-control'}))
    phone = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'placeholder': '600700800', 'class':'form-control'}))
    title = forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'placeholder': 'urodziny janka', 'class':'form-control'}))
    term_of_reservation = forms.DateTimeField(label="Termin rezerwacji", widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS', 'class':'form-control'}))
    bar = forms.ModelChoiceField(label='', queryset=Bar.objects.all(), widget=forms.Select(attrs={ 'class':'form-control'}))   
    nr_of_people = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'ile osob?', 'class':'form-control'}))
    catering = forms.BooleanField(label='Catering:', required=False)
    faktura = forms.BooleanField(label='Faktura', required=False)
    additional_information = forms.CharField(label='', required=False, max_length=250, widget=forms.TextInput(attrs={'placeholder': 'dodatkowe informacje', 'class':'form-control'}))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'title', 'term_of_reservation', 'bar', 'nr_of_people','additional_information', 'catering', 'faktura']


