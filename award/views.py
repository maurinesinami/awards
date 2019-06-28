from django.shortcuts import render
from django.http  import HttpResponse
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request,'welcome.html')
