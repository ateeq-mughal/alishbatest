from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {                    #For variable value and then add this in render parameter, step 23 django notes
        "variable1":"This is just the start" ,
        "variable2":"This is another variable" 
    }
    
    return render(request, 'index.html', context) #template name to direct the user to html page
#  return HttpResponse("This is Home Page") #This will show on our home website page; step 14 in django notes

def about(request):
    return render(request, 'about.html')
   # return HttpResponse("This is about our Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,password=password,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted. Thankyou for trusting us!')

    return render(request, 'contact.html')
   # return HttpResponse("Contact us here")