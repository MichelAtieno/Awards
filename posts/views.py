from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                redirect('login.html')
    else:
        form=RegistrationForm()
        return render(request, 'registration/registration_form.html', {'form':form})
