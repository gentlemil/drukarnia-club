from django import forms
from .models import Reservation, Bar

class ReservationForm(forms.ModelForm):

    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Jan Kowalski'}))
    email = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'jan@kowalski.com'}))
    phone = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': '600700800'}))
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'urodziny janka'}))
    term_of_reservation = forms.DateTimeField(label="Termin rezerwacji: ", widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
    bar = forms.ModelChoiceField(label="Bar:", queryset=Bar.objects.all(), widget=forms.Select())   
    nr_of_people = forms.IntegerField(label="Liczba osob:")
    catering = forms.BooleanField(required=False)
    faktura = forms.BooleanField(required=False)
    additional_information = forms.CharField(required=False, max_length=250, widget=forms.Textarea(attrs={'placeholder': 'dodatkowe informacje'}) )

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'title', 'term_of_reservation', 'bar', 'nr_of_people','additional_information', 'catering', 'faktura']


