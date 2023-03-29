from django.shortcuts import render, redirect,HttpResponse
from datetime import datetime
from hospital_app.models import appointment
from django.contrib import messages
from django.utils import timezone
import datetime
# Create your views here.


def home_page(request):
    return render(request, 'front_page.html')

def specialties(request):
    return HttpResponse("Working on specilaties")

def doctors(request):
    return HttpResponse("Working on doctors")

def contact_us(request):
    return HttpResponse("Working on contact page")

def about_us(request):
    return HttpResponse("Working on about info")




def book_appointment(request):
    if request.method == 'POST':
        print("req received")
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        doctor = request.POST.get('doctor')
        date = timezone.now() # get current date 
        time = datetime
        # appointment.objects.create(created_at=current_datetime)
        # date = request.POST.get('date')
        # time = request.POST.get('time')
        obj = appointment(name=name, age=age,gender=gender,email=email,
                          phonenumber=phonenumber,doctor=doctor,date=date )
        print("adityaaaaaaaaaaaaaaaaaaaaaaa")
        obj.save()      # used to save the form data in database
        # messages.success(request,'done sumbitting')
        # print("helooooooooooooooooooo")
        messages.success(request, 'form submitted succesfully')
        return render(request, 'book_appointment.html', {'messages': messages.get_messages(request)})
        # messages.info(request,'form submitted succesfully')     #returns a response to the user using messages.info() method.
        # print(messages.get_messages(messages))
    return render(request, 'book_appointment.html')
