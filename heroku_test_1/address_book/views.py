from django.shortcuts import redirect, render


def home(request):
    return render(request, "home.html", {})


def add_address(request):
    return render(request, "add_address.html", {})
