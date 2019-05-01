
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def logout(request):
    return redirect('home')
    # Redirect to a success page.