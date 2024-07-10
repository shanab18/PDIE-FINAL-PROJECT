from django.shortcuts import render, redirect
from sporthub.models import Student, Admin, Facility, Booking
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def loginstudent(request):
    if request.method == 'POST':
        idstudent = request.POST['studentid']
        wordpass = request.POST['password']
        # Check if student exists and credentials are correct
        if Student.objects.filter(studentid=idstudent, password=wordpass).exists():
            # Store student ID in session
            request.session['student_id'] = idstudent
            # Redirect to the home page
            return redirect('home')
        else:
            # Handle invalid credentials
            return render(request, 'loginstudent.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'loginstudent.html')


def loginadmin(request):
    if request.method == 'POST':
        idadmin = request.POST['adminid']
        passwordad = request.POST['adpassword']
        # Check if admin exists and credentials are correct
        if Admin.objects.filter(adminid=idadmin, adpassword=passwordad).exists():
            # Redirect to the admin home page
            return redirect('homeadmin')
        else:
            # Handle invalid credentials
            return render(request, 'loginadmin.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'loginadmin.html')

def logout(request):
    return redirect('loginstudent')

def home(request):
    context = {

    }
    return render (request, "home.html", context)

def homeadmin(request):
    return render(request,'homeadmin.html')

def facility(request):
    return render(request,'facility.html')

def facilityadmin(request):
    return render(request,'facilityadmin.html')

def booking(request):
    if request.method == 'POST':
        studentname = request.POST['studentname']
        studentid = request.POST['studentid']
        phonenumber = request.POST.get('phonenumber')
        facility = request.POST.getlist('facility[]')
        datestarts = request.POST.getlist('datestart[]')
        dateends = request.POST.getlist('dateend[]')
        quantity = request.POST.getlist('quantity[]')

        # Create a new booking entry for each facility
        for fac, start, end, qty in zip(facility, datestarts, dateends, quantity):
            if fac != 'select':
                facility = Facility.objects.get(facname=fac)
                bookingid = generate_unique_booking_id()
                new_booking = Booking(
                    bookingid=bookingid,
                    studentname=studentname,
                    bookstudent=Student.objects.get(studentid=studentid),
                    phonenumber=phonenumber,
                    bookfac=facility,
                    datestart=start,
                    dateend=end,
                    quantity=qty
                )
                new_booking.save()
        messages.success(request, 'Booking successfully created.')
        return redirect('historybook')
    # Assuming student ID is stored in the session
    studentid = request.session.get('student_id', '')
    return render(request, 'booking.html', {'studentid': studentid})
        
        #bookstudent = Student.objects.get(studentid=bookstudent)
        #facid = Facility.objects.get(bookfac=facid)
        #databooking = Booking(bookingid=bookingid, studentname=studetname, bookstudent=bookstudent, bookfac=bookfac)
        #databooking.save()
        #return HttpResponseRedirect('historybooking.html')
    #else:
       # context = {
        #    'allbooking': allbooking,
        #}
        #return render(request, 'booking.html', context)

def historybook(request):
    allbooking = Booking.objects.all()
    context = {
        'allbooking' : allbooking
    }
    return render(request, 'historybook.html', context)


def bookingadmin(request):
    adminbooking = Booking.objects.all()
    context = {
        'adminbooking' : adminbooking
    }
    return render(request, 'bookingadmin.html', context)

import uuid
def generate_unique_booking_id():
    return str(uuid.uuid4()).replace('-', '')[:15]


def newfacility(request):
    return render(request,'newfacility.html')




#def approve_booking(request, bookingid):
#    booking = Booking.objects.get(pk=bookingid)
    # Update the booking status to "Approved" (assuming you have a field for status)
#    booking.status = 'Approved'
#    booking.save()
#    return redirect('admin_booking')

#def reject_booking(request, booking_id):
#    booking = Booking.objects.get(pk=bookid)
    # Update the booking status to "Rejected" (assuming you have a field for status)
#    booking.status = 'Rejected'
#    booking.save()
#    return redirect('admin_booking')

