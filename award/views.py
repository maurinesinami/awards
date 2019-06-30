from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from . models import  Profile
from django.contrib.auth.models import User
from .forms import NewProfileForm
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request,'welcome.html')
@login_required(login_url='/accounts/login/')      
def new_profile(request,id):
    user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form":form,"user":user})
