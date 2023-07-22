from django.shortcuts import render,redirect
from .models import Customer
from .forms import RegisterForm,ContactForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def cart(request):
    return render(request,'cart.html')

def contact(request):
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact.html',{'form':ContactForm,'result':'success'})
        return render(request,'contact.html',{'form':form,'result':'fail'})
    return render(request,'contact.html',{'form':form})








def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer.user)
            return redirect('shop:index')
        return render(request, 'register.html', {'form': form,'result':'success'})
    
    return render(request, 'register.html', {'form': form})




def login_view(request):
     form = LoginForm()
     if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username ,password=password)
             if user is not None:
                 login(request,user)
                 return redirect('shop:index')
             return render(request, 'login.html', {'form': form, 'result': 'fail'})
     else:
        return render(request, 'login.html', {'form': form})


    
def logout_view(request):
    logout(request)
    return redirect('customer:login')

    
