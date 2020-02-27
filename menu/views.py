from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin   #CBV
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import TypeOfProduct, Product

# from django.contrib.auth.decorators import login_required   #FBV
# from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import Sum, DateField, Count
# from django.db.models.functions import TruncDate
# from .forms import ReservationForm

# -------------------------------------------------------------------------
def index(request):
    categories = TypeOfProduct.objects.all().prefetch_related('product')
    # ---
    # menus = Product.objects.all()
    # kinds = TypeOfProduct.objects.all()
    context = {
        'categories': categories,
        # 'menus': menus,
        # 'kinds': kinds
    }
    return render(request, 'menu/menuindex.html', context) 
# -------------------------------------------------------------------------

class MenuCreate(LoginRequiredMixin, CreateView):
    model = TypeOfProduct, Product
    fields = ['name', 'amount', 'prize']
    template_name= 'menu/menucreate.html'

class MenuUpdate(LoginRequiredMixin, UpdateView):
    model = TypeOfProduct, Product
    fields = ['name', 'amount', 'prize']
    template_name = 'menu/menuupdate.html'
    

class MenuDelete(LoginRequiredMixin, DeleteView):
    model = TypeOfProduct, Product
    template_name = 'menu/menudelete.html'

    # def get_success_url(self):
    #     return reverse_lazy('confirm')

