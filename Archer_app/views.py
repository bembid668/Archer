from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,  authenticate, logout
from django.contrib.auth.models import User
from Archer_app.forms import AuthenticateForm, UserCreateForm, ArcherForm
from Archer_app.models import Archer


def index(request, auth_form=None, user_form=None):
    if request.user.is_authenticated():
        Archer_form = ArcherForm()
        user = request.user
        Archers_self = Archer.objects.filter(user=user.id)
        Archers_buddies = Archrr.onjects.filter(user_userprofile_in=user.profile.follows.all)
        Archers = Archers_self | Archers_buddies

        return render(request,
                      'buddies.html',
                      {'Archer_form': Archer_form, 'user': user,
                       'Archers': Archers,
                       'next_rul': '/',})


    else:
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
                      'home.html',
                      {'auth_form' :auth_form, 'user_form' : user_form, })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        return index(request, user_form=user_form)
    return redirect('/')
# Create your views here.
