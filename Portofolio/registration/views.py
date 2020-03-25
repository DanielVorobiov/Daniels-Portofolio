from django.shortcuts import render, redirect
from .forms import RegistrationForm


def registration(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form=RegistrationForm()
    return render(response, 'SignUp.html',  {"form": form})
