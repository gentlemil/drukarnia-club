from django.contrib.auth.mixins import LoginRequiredMixin   #CBV
from django.contrib.auth.decorators import login_required   #FBV
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum, DateField, Count
from django.db.models.functions import TruncDate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from .forms import ReservationForm
from .models import Reservation, Bar

# /reservation --- glowny widok aplikacji rezerwacji, gdzie beda wyswietlane mozliwe akcje do wyboru
def index(request):

    return render(request, 'reservation/index.html')


# /reservation/create/
def reservation_create(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            r = form.save()
            return redirect(reverse('reservation_details', args=[r.pk]))
    else:
        form = ReservationForm()     # ---> trzeba zaimportowac suggestionform
   
    context = {
        'title': 'Sugestia ankiety',
        'form': form,

    }
    return render(request, 'reservation/create.html', context)


# /reservation/list --- widok wyswietlajacy wszystkie powstale rezerwacje.
# @login_required
def reservation_list(request):

    reservations = Reservation.objects.all().order_by('term_of_reservation')
    context = {

        'reservations': reservations
    }
    return render(request, 'reservation/list.html', context)


# /reservation/id --- widok pokazujacy szczegoly dot. konkretnej rezerwacji
# @login_required
def reservation_details(request, pk):

    rd = get_object_or_404(Reservation, pk=pk)
    context = {
        'title': rd.name,
        'reservation': rd,
    }
    return render(request, 'reservation/details.html', context)


# /reservation/id/edit --- widok do edycji rezerwacji (po stronie admina oczywiscie)
class ReservationEdition(LoginRequiredMixin, UpdateView):

    model = Reservation
    fields = ['title', 'name', 'email', 'phone', 'term_of_reservation', 'bar',
    'nr_of_people', 'catering', 'faktura', 'additional_information', 'status']
    template_name = 'reservation/edition.html'


# /reservation/id/delete --- widok do usuwania rezerwacji (po stronie admina oczywiscie)
class ReservationDelete(LoginRequiredMixin, DeleteView):

    model = Reservation
    template_name = 'reservation/delete.html'

    def get_success_url(self):
        return reverse_lazy('confirm')


# /reservation/bar-availability/ --- widok pokazujacy ilosc wolnych miejsc
# @login_required
def bar_availability(request):

    reservations = Reservation.objects.all().order_by('-term_of_reservation')

    nr_days = Reservation.objects \
        .annotate(day=TruncDate('term_of_reservation', output_field=DateField())).distinct() \
        .values_list('day', flat=True)
    result = Bar.objects.annotate \
        (day=TruncDate('reservation__term_of_reservation', output_field=DateField())) \
            .annotate(people=Sum('reservation__nr_of_people')).order_by('pk', 'day')
    results2 = result.values_list()
    results2 = list(zip(*results2))
    context = {
        'result': result,
        'results2': results2,
        'nr_of_days': nr_days,
    }
    return render(request, 'reservation/availability.html', context)

# /reservation/confirm/ --- widok potwierdzenia zlozenia rezerwacji
class ConfirmReservation(TemplateView):

    template_name = "reservation/confirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
