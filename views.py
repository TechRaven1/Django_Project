from django.shortcuts import render
from django.http import HttpResponse

from .models import ug_new_arrivals


def homepage(request):
    new_prods = ug_new_arrivals.objects.all()
    return render(request, 'home2.html', {'ug_new_arrivals': new_prods})


def blog(request):
    return render(request, 'blog.html')


def blog1(request):
    return render(request, 'blog-detail.html')


def about(request):
    return render(request, 'about-us.html')


def cart(request):
    return render(request, 'cart-page.html')


def contact(request):
    return render(request, 'contact-us.html')


def shop(request):
    return render(request, 'shop.html')


def shop1(request):
    return render(request, 'shop-detail.html')


def user_register(request):
    return render(request, 'register.html')


def user_login(request):
    return render(request, 'login.html')


def potting_soil(request):
    return render(request, 'potting_soil.html')


def plant_health(request):
    return render(request, 'plant_health.html')


def seeds(request):
    return render(request, 'seeds.html')


def accessories(request):
    return render(request, 'accessories.html')


def services(request):
    return render(request, 'services.html')


def home(request):
    return render(request, 'home2.html')


def view_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass
