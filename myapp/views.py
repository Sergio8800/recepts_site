from datetime import date, timedelta

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def index_start_app(request):
    products = Recept.objects.all().order_by('-date_added')
    context = {
        'title': "Recepts of all clients",
        'products': products,
    }

    return render(request, 'myapp/index_start_app.html', context=context)
    # return render(request, 'myapp/index_start_app.html', {"products_lst": products_lst})


def index_ord_filtr(request):
    today = date.today() - timedelta(days=1)
    order_filtr = Recept.objects.filter(date_ordered__gte=today)
    # order_filtr = Order.objects.exclude(date_ordered__gte=today) # исключить все записи удовлетворяющие условию
    context = {
        'title': "Orders of all clients",
        'diapason': f' не вошли заказы меньше этой даты: {today}',
        'orders': order_filtr,
    }
    return render(request, 'myapp/index_orders1.html', context)


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = "Error data"
        if form.is_valid():
            form.save()
            return redirect('product_form')
    else:
        form = ProductForm()
        message = "Input product"

    return render(request, 'myapp/product_form.html', {'form': form, 'message': message})


def product_form_update(request, product_id):
    # intention = Product.objects.get(pk=product_id)
    intention = get_object_or_404(Recept, pk=product_id)
    message = 'change data'
    form = ProductForm(instance=intention)  # important for entre DATA
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # important for entre DATA

        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()

            Recept.objects.filter(pk=product_id).update(name=name, category=category, description=description,
                                                        price=price, quantity=quantity,
                                                        image=fs.save(image.name, image))

            message = ' data is change '
            # return redirect('index_start')

    return render(request, 'myapp/product_form_update.html', {'form': form, 'message': message})


def product_detail(request, product_id):
    product = Recept.objects.get(pk=product_id)
    template_name = 'myapp/product_detail.html'
    context = {'product': product}
    return render(request, template_name, context)


def deleteView(request, product_id):
    obj = Recept.objects.get(pk=product_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('index_start')
    template_name = 'myapp/product_del.html'
    context = {'obj': obj}
    return render(request, template_name, context)


def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        message = "Error data"
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = Category(name=name)
            cat.save()
            form.clean()
            message = f'Категория {cat.name} save in DB'
            # return redirect(category_form)
    else:
        form = CategoryForm()
        message = "Input category"
    return render(request, 'myapp/category_form.html', {'form': form, 'message': message})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('loginform')

    # эта функция для автоматической аунтификации на сате после регистрации.
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index_start_app')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'myapp/login.html'

    def get_success_url(self):
        return reverse_lazy('index_start_app')


def logout_user(request):
    logout(request)
    return redirect('loginform')
