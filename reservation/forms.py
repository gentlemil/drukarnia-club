from django import forms
from .models import Reservation, Bar

# --- formularz logowania sie

# --- formularz tworzenia nowej rezerwacji
class ReservationForm(forms.ModelForm):

    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Podaj Imie i Nazwisko'}))
    email = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Podaj adres e-mail'}))
    phone = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Podaj swoj nr'}))
    term_of_reservation = forms.DateTimeField(label="Termin rezerwacji: ", widget=forms.TextInput(attrs={'placeholder': 'Podaj termin'}))
    bar = forms.ModelChoiceField(label="Bar:", queryset=Bar.objects.all(), widget=forms.Select())
    nr_of_people = forms.IntegerField(label="Liczba osob:")
    catering = forms.BooleanField(label="Catering:")
    faktura = forms.BooleanField(label="Faktura:")
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Podaj Imie i Nazwisko'}))
    additional_information = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'placeholder': 'drogi pamietniczku'}) )

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'term_of_reservation', 'bar', 'nr_of_people', 'catering', 'faktura', 'additional_information']


