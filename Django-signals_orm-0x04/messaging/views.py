from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()  # Required for the check
    return redirect('home')  # Replace 'home' with your desired redirect URL

# Create your views here.
