from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about.html')

def auth(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'login':
            # Process login data
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                return redirect('dashboard')
            else:
                return redirect('/')
            # Add your user authentication logic here
        elif action == 'signup':
            # Process and save signup data
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            
       
            print(f"Signup for {full_name} with email: {email} - User saved to DB.")
            # Add your user creation logic here
            return redirect('dashboard')
            
    return render(request, 'auth.html')

def billing(request):
    return render(request, 'billing.html')

def change_pass(request):
    return render(request, 'change-password.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def pulls(request):
    return render(request, 'pulls.html')

@login_required
def repo(request):
    return render(request, 'repo.html')

def settings(request):
    return render(request, 'settings.html')

def api_docs(request):
    return render(request, 'api.html')

def blog(request):
    return render(request, 'blog.html')

@login_required
def notepad(request):
    return render(request, 'notepad.html')

def career(request):
    return render(request, 'careers.html')

def community(request):
    return render(request, 'community.html')

def contact_us(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def change_pass(request):
    return render(request, 'change_pass.html')

def security(request):
    return render(request, 'security.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def help_center(request):
    return render(request, 'help.html')

def system_status(request):
    return render(request, 'status.html')

def terms_condition(request):
    return render(request, 'terms.html')

@login_required
def logouts(request):
    logout(request)
    return redirect('/')

def signup_form(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        print(full_name, email, password)
        return redirect('/dashboard')
    return render(request, 'signup.html')