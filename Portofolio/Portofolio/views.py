from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



def home(request):
    return render(request, 'Home.html')


def login(request):
    return render(request, "Login.html")


def signup(request):
    return render(request,"SignUp.html")

def gallery(request):
    return render(request, "Gallery.html")

def about(request):
    return render(request, "About.html")


def contact(request):
    form = ContactForm()
    if request.method =="POST":
        form =  ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ["vorobiov.daniel@gmail.com","balaurdorina@gmail.com"]
            try:
                send_mail(subject,message,sender,recipients,fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header form')
            return HttpResponse('Success...Your email has been sent')
    return render(request, "Contact.html",{"form": form})