from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return redirect('about')
    # else:
        products=product.objects.all()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('about')
            else:
                messages.info(request, 'Incorrect username and password')
            
        # return HttpResponse("<h1>Hello World!</h1>")
        return render(request,'index.html',{'products': products})

@login_required(login_url='index')
def about(request):
    # if request.user.is_authenticated:
    #     return redirect('about')
    # else:
        return render(request,'about.html')

def logoutuser(request):
    logout(request)
    return redirect('index')