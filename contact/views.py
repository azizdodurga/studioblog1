from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def emailView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data["mail"]
            message = form.cleaned_data["message"]
            form.save()
            messages.success(request, "we have receieved your message successfully")
            return redirect("contact")
    else:
        form = ContactForm()
    return render (request, "contact.html", {"form":form})
