from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)

def score_increase(requst, user_pk):
    user = User.objects.get(pk=user_pk)
    user.score += 100
    user.save()
    return redirect('accounts:index')