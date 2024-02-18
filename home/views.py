from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "owner1":"Mukhtar",
        "owner2":"Islam",
        "owner3":"Tausif",
    }
    return render(request, "index.html", context )

# return HttpResponse("This is Homepage")

def about(request):
    return render(request, "about.html" )

    # return HttpResponse("This is About Page")

def services(request):
    return render(request, "services.html" )

    # return HttpResponse("This is SERVICES page")

def contact(request):
    if request.method == "POST": #name
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Message = request.POST.get("Message")
        contact = Contact(name=name, email=email, phone=phone, Message=Message, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent!")

    return render(request, "contact.html" )

    # return HttpResponse("This is Contact Page")

def blog(request):
    return render(request, "blog.html" )
