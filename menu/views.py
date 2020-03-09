from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin   #CBV
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Sum, DateField, Count
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .forms import ProductForm
from .models import TypeOfProduct, Product

# /menu --- glowny widok, widoczny dla wszystkich
def index(request):
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')

    context = {
        'categories': categories,  
    }
    return render(request, 'menu/menuindex.html', context) 


# /menu/list/
# @login_required
def menu_list(request):

    products = Product.objects.all().order_by('price')
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'menu/menuproductlist.html', context)


# class MenuCreate(LoginRequiredMixin, CreateView):
#     model = TypeOfProduct, Product
#     fields = ['name', 'amount', 'prize']
#     template_name= 'menu/menucreate.html'

# @login_required
def menu_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            r = form.save()
            return redirect(reverse('menu_details', args=[r.pk]))
    else:
        form = ProductForm()     # ---> trzeba zaimportowac suggestionform
   
    context = {
        'title': 'Sugestia ankiety',
        'form': form,
    }
    return render(request, 'menu/menucreate.html', context)

# @login_required
def menu_details(request, pk):

    rd = get_object_or_404(Product, pk=pk)
    # products = Product.objects.all().order_by('price')
    # categories = TypeOfProduct.objects.all().prefetch_related('product_set')
    
    context = {
        'title': rd.name,
        'product': rd,
        # 'categories': categories,
        # 'products': products,

    }
    return render(request, 'menu/menudetails.html', context)

class MenuDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'menu/menudelete.html'

    def get_success_url(self):
        return reverse_lazy('confirm')


class ConfirmMenuPage(TemplateView):

    template_name = "menu/menuconfirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context