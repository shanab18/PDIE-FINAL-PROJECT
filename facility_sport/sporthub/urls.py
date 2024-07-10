from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginstudent/', views.loginstudent, name='loginstudent'),
    path('loginadmin/', views.loginadmin, name='loginadmin'),
     path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('homeadmin/', views.homeadmin, name='homeadmin'),
    path('facility/', views.facility, name='facility'),
    path('facilityadmin/', views.facilityadmin, name='facilityadmin'),
    path('newfacility/', views.newfacility, name='newfacility'),
    path('booking/', views.booking, name='booking'),
    path('bookingadmin/', views.bookingadmin, name='bookingadmin'),
    path('historybook/', views.historybook, name='historybook'),
    #path('approve-booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    #path('reject-booking/<int:booking_id>/', views.reject_booking, name='reject_booking'),
]


 