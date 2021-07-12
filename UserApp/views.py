from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SingUpCreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.urls import reverse


def SingUp(request):
    form = SingUpCreateUserForm()
    if request.method == 'POST':
        form = SingUpCreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully .')
            return HttpResponseRedirect(reverse('UserApp:log_in'))

    data = {
        "title": "sing_up page",
        "form": form,
    }
    return render(request, 'AppUser/sing_up.html', data)


def Login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        error_messages = None
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # session er code  start
                request.session['Customer'] = user.id
                # session End
                return redirect('AppShopStore:homepage')
                # Redirect to a success page.
            else:
                return redirect(request.build_absolute_uri())  # current page redirect

        # Return an 'invalid login' error message.
    data = {
        "form": form,
    }
    return render(request, 'AppUser/login.html', data)


def LogOUt(request):
    request.session.clear()
    # logout(request)
    # messages.warning(request, 'Your are logged Out')
    return HttpResponseRedirect(reverse('AppShopStore:homepage'))
