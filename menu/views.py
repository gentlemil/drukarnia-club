from django.shortcuts import render
from . import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Sum, DateField, Count
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .forms import ProductForm #TypeOfProductForm
from .models import TypeOfProduct, Product

def index(request):
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')

    context = {
        'categories': categories,  
    }
    return render(request, 'menu/menuindex.html', context) 

def menu_list(request):
    products = Product.objects.all().order_by('price').order_by('prize')
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'menu/menuproductlist.html', context)

# ------------------------------------------------
# ------ CREATING NEW PRODUCT / CATEGORY ---------

# @login_required
def menu_create(request):
    typeofproduct = TypeOfProduct.objects.all()
    products = Product.objects.all().order_by('price').order_by('name')
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            r = form.save()
            return redirect(reverse('menu_details', args=[r.pk]))
    else:
        form = ProductForm()
   
    context = {
        'typeofproduct': typeofproduct,
        'categories': categories,
        'products': products,
        'form': form,
    }
    return render(request, 'menu/menucreate.html', context)

# @login_required
def menu_category_create(request):
    typeofproduct = TypeOfProduct.objects.all()
    products = Product.objects.all().order_by('price').order_by('name')
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')

    if request.method == 'POST':
        form = TypeOfProductForm(request.POST)
        if form.is_valid():
            r = form.save()
            return redirect(reverse('menu_category_details', args=[r.pk]))
    else:
        form = TypeOfProductForm()
   
    context = {
        'typeofproduct': typeofproduct,
        'categories': categories,
        'products': products,
        'form': form,
    }
    return render(request, 'menu/menucreate-category.html', context)

# ------------------------------------------------
# ------ DETAILS OF THE PRODUCT / CATEGORY -------

# @login_required
def menu_details(request, pk):
    rd = get_object_or_404(Product, pk=pk)
    products = Product.objects.all().order_by('price')
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')
    context = {
        'title': rd.name,
        'product': rd,
        'categories': categories,
        'products': products,
    }
    return render(request, 'menu/menudetails.html', context)

# @login_required
def menu_category_details(request, pk):
    rd = get_object_or_404(Product, pk=pk)
    products = Product.objects.all().order_by('price')
    categories = TypeOfProduct.objects.all().prefetch_related('product_set')
    context = {
        'title': rd.name,
        'product': rd,
        'categories': categories,
        'products': products,
    }
    return render(request, 'menu/menudetails-category.html', context)

# ---------------------------------------------
# --------- UPDATE PRODUCT / CATEGORY ---------

class MenuUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'prize', 'types', 'description']
    # form_class = 'form-control'
    template_name = 'menu/menuupdate.html'

    def get_success_url(self):
        return reverse_lazy('menu_confirm')

# ---------------------------------------------
# --------- DELETE PRODUCT / CATEGORY ---------

class MenuDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'menu/menudelete.html'

    def get_success_url(self):
        return reverse_lazy('menu_confirm')

class MenuCategoryDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'menu/menudelete-category.html'

    def get_success_url(self):
        return reverse_lazy('menu_category_confirm')

# ---------------------------------------------------
# --- CONFIRM DONE WORK WITH A PRODUCT / CATEGORY ---

class ConfirmMenuPage(TemplateView):

    template_name = "menu/menuconfirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ConfirmMenuCategoryPage(TemplateView):

    template_name = "menu/menuconfirm-category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context