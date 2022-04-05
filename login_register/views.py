from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from login_register.forms import Login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
def login_view(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    return HttpResponse('sorry,you\'re not active ')
            else:
                return HttpResponse('Invalid Login')
        else: 
            return HttpResponse('somethong goes wrong')
    else:
        form = Login()
    return render(request, 'accounts/login.html', {'form': form})


class register(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user_registration.html'
    def form_valid(self, form):
        form.save()
        return super(register, self).form_valid(form)

def authenticated(request):
    return render(request, "authenticated.html")

def logout_view(request):
    logout(request)
    return redirect('login')