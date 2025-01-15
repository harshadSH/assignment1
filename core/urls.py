from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('patient/signup/', views.patient_signup, name='patient_signup'),
    path('doctor/signup/', views.doctor_signup, name='doctor_signup'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
