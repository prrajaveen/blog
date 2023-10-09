from django.shortcuts import render,HttpResponse

def login(request):
    return render(request , 'accounts/login.html')
