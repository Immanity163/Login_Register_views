from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from login_register.forms import Login

def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],password = cd[password])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated')
                else:
                    return HttpResponse('some error(actually not)')
            else:
                return HttpResponse('Invalid Login')
        else: 
            return HttpResponse('somethong goes wrong')
    else:
        form = Login()
    return render(request, 'accounts/login.html', {'form': form})

