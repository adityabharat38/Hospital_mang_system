from django.shortcuts import render, redirect,HttpResponse
from datetime import datetime
from hospital_app.models import appointment
from django.contrib import messages
from django.utils import timezone
from pathlib import Path
import datetime
import time
# Create your views here.


def home_page(request):
    return render(request, 'front_page.html')

def specialties(request):
    return render(request,'specialities.html')

def doctors(request):
    return render(request,'doctors.html')

def contact_us(request):
    return render(request,'contact_us.html')

def about_us(request):
    return render(request,'about_us.html')




def book_appointment(request):
    if request.method == 'POST':
        print("req received")
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        doctor = request.POST.get('doctor')
        current_datetime = datetime.datetime.now()
        print(request.POST)
        # here i named the variable new_time to demonstarte that we can choose independent names here ,but when
        # we pass them on object for model class , we are now giving their value to model class variables that are
        # representing the database (rows and coloums)

        obj = appointment(name=name, age=age,gender=gender,email=email,
                          phonenumber=phonenumber,doctor=doctor,datetime = current_datetime)
        print("req completed succesfully")

        check = obj.save()      # used to save the form data in database

        print(check)    # it is none see reason below
        # When you call obj.save(), the object is saved to the database, and its primary key (pk) is assigned. 
        # However, the save() method does not return the object instance. Instead, it returns None by default, 
        # indicating that the object was saved successfully.
        try:
            if obj.pk:
                print("data stored in databse sucessfully")

        except Exception as e :
            print(e)

        messages.success(request, 'form submitted succesfully')
        # return render(request, 'book_appointment.html', {'messages': messages.get_messages(request)})
        # messages.info(request,'form submitted succesfully')     #returns a response to the user using messages.info() method.
        # print(messages.get_messages(messages))
        return redirect(request.path)
    return render(request, 'book_appointment.html')
