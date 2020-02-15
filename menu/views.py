from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin   #CBV
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Menu

# from django.contrib.auth.decorators import login_required   #FBV
# from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import Sum, DateField, Count
# from django.db.models.functions import TruncDate
# from .forms import ReservationForm

def index(request):
    menus = Menu.objects.all().order_by('type').order_by('name')
    context = {
        'menus': menus
    }
    
    return render(request, 'menu/menuindex.html', context) 

class MenuCreate(LoginRequiredMixin, CreateView):
    model = Menu
    fields = ['name', 'kind', 'amount', 'prize']
    template_name= 'menu/menucreate.html'

class MenuUpdate(LoginRequiredMixin, UpdateView):
    model = Menu
    fields = ['name', 'kind', 'amount', 'prize']
    template_name = 'menu/menuupdate.html'
    

class MenuDelete(LoginRequiredMixin, DeleteView):
    model = Menu
    template_name = 'menu/menudelete.html'

    # def get_success_url(self):
    #     return reverse_lazy('confirm')

