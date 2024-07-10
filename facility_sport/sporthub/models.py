from django.db import models

# Create your models here.

class Student(models.Model):
    studentid=models.CharField(max_length=15, primary_key=True)
    password=models.CharField(max_length=8)
    
class Admin(models.Model):
    adminid=models.CharField(max_length=15, primary_key=True)
    adpassword=models.CharField(max_length=8)

class Facility(models.Model):
    facid=models.CharField(max_length=15, primary_key=True)
    facname=models.TextField(max_length=30)
    quantity=models.IntegerField()


class Booking(models.Model):
    bookingid=models.CharField(max_length=15, primary_key=True)
    studentname=models.TextField(max_length=100)
    bookstudent=models.ForeignKey('Student', on_delete=models.CASCADE, null=True)
    phonenumber=models.CharField(max_length=15)
    bookfac = models.ForeignKey('Facility', on_delete=models.CASCADE, null=True)
    datestart=models.DateField()
    dateend=models.DateField()
    quantity=models.IntegerField()