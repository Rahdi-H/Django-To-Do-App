from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, LoginForm
from .models import ToDo

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            todo = request.POST['todo']
            ToDo(todo=todo, author=request.user).save()
        data = ToDo.objects.all().filter(author=request.user)
        return render(request, 'core/home.html', {'data':data})
    else:
        return redirect('login')
    
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'core/register.html', {'form':form})
    else:
        return redirect('home')
    
def signIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=username, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'core/login.html', {'form':form})
    else:
        return redirect('home')

def signOut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
    
def deleteData(request, id):
    if request.user.is_authenticated:
        data = ToDo.objects.get(pk=id)
        data.delete()
        return redirect('home')
    else:
        return redirect('login')

def updateData(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ToDo(id=id, todo=request.POST['todo'], author=request.user).save()
            return redirect('home')
        else:
            data = ToDo.objects.get(pk=id)
            return render(request, 'core/update.html', {'data':data})
    else:
        return redirect('login')