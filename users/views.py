from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created. Please Login.')
            return redirect('user-login')
    else:
        form = UserRegistrationForm()


    return render(request, 'users/register.html', {'form' : form})


@login_required
def profile(request):
    return render(request,'users/profile.html', {})

