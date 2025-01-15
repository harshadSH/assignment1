from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Patient, Doctor
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def patient_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('patient_signup')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            Patient.objects.create(
                user=user,
                profile_picture=profile_picture,
                address=address,
            )
            messages.success(request, "Patient signup successful! Please log in.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('patient_signup')

    return render(request, 'patient_signup.html')


def doctor_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('doctor_signup')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            Doctor.objects.create(
                user=user,
                profile_picture=profile_picture,
                address=address,
            )
            messages.success(request, "Doctor signup successful! Please log in.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('doctor_signup')

    return render(request, 'doctor_signup.html')

def home_page(request):
    if request.method == 'POST':
        # Handling login for patient
        if 'patient_login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user and hasattr(user, 'patient'):
                auth_login(request, user)
                return redirect('patient_dashboard')

        # Handling login for doctor
        elif 'doctor_login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user and hasattr(user, 'doctor'):
                auth_login(request, user)
                return redirect('doctor_dashboard')

    # Handle signup


    return render(request, 'home.html', )

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
