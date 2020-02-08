from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Bar
from django.views.generic import CreateView, UpdateView, DeleteView

from django.db.models import Count

from django.contrib.auth.mixins import LoginRequiredMixin   #CBV
from django.contrib.auth.decorators import login_required   #FBV

from django.db.models import Sum, DateField
from django.db.models.functions import TruncDate

from .forms import ReservationForm

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView

from django.urls import reverse

# glowny widok aplikacji rezerwacji, gdzie beda wyswietlane mozliwe akcje do wyboru
# /reservation
def index(request):
    return render(request, 'reservation/index.html')

# widok wyswietlajacy wszystkie powstale rezerwacje.
# /reservation/list
@login_required
def reservation_list(request):
    reservations = Reservation.objects.all().order_by('-term_of_reservation')
    context = {

        'reservations': reservations
    }
    return render(request, 'reservation/list.html', context)

# widok pokazujacy szczegoly dot. konkretnej rezerwacji
# /reservation/id
@login_required
def reservation_details(request, pk):
    rd = get_object_or_404(Reservation, pk=pk)
    context = {
        'title': rd.name,
        'reservation': rd,
    }
    return render(request, 'reservation/details.html', context)

# widok do edycji rezerwacji (po stronie admina oczywiscie)
# dorobic pozniej wyswietlanie komunikatu ze zmiany zostaly wprowadzone pomylsnie
# /reservation/id/edit
class ReservationEdition(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = ['name', 'phone', 'term_of_reservation', 'bar', 'nr_of_people', 'status']
    template_name = 'reservation/edition.html'

# widok do usuwania rezerwacji (po stronie admina oczywiscie)
# /reservation/id/delete
class ReservationDelete(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservation/delete.html'

# widok formularzu do tworzenia nowej rezerwacji
# /reservation/create/
# class ReservationCreate(CreateView):
#     model = Reservation
#     fields = ['name', 'email', 'phone', 'term_of_reservation', 'bar', 'nr_of_people', 'catering', 'faktura', 'additional_information']
#     template_name = 'reservation/create.html'


# widok pokazujacy ilosc wolnych miejsc
# /reservation/bar-availability/
@login_required
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

    # for bar in Bar.objects.annotate(day=TruncDate('reservation__term_of_reservation', output_field=DateField()))
    #  .annotate(people=Sum('reservation__nr_of_people')):
    #      print(bar, bar.day, bar.people)

# /reservation/create/
def reservation_create(request):
    # jesli sa dane POST to sprobuj je zwalidowac
    if request.method == 'POST':
        # skoro sa dostepne dane POST, to nalezy je wrzcic do formularza
        form = ReservationForm(request.POST)
        # sprawdzenie poprawnosci formularza
        if form.is_valid():

            r = form.save()

            # messages.success(request, 'SUKCES SUKCES SUKCES')   #formul. przeszedl walidacje :)
            # return redirect(q.get_absolute_url())
            return redirect(reverse('reservation_details', args=[r.pk]))

        else:       #formularz nie przeszedl walidacji, czyli ma bledy
            messages.error(request, 'BLAD BLAD BLAD!')


    # nie ma danych POST wiec pokazujemy pusty formularz
    else:
        form = ReservationForm()     # ---> trzeba zaimportowac suggestionform

    # DLA TESTOW
    # messages.debug(request, 'info dla programistow')
    # messages.info(request, 'info informacyjne')
    # messages.warning(request, 'uwaga')
    
    context = {
        'title': 'Sugestia ankiety',
        'form': form,
    }
    return render(request, 'reservation/create.html', context)

class ConfirmPage(TemplateView):

    template_name = "reservation/confirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context