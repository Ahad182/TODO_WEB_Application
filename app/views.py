from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as Userlogin,logout

from app.forms import TODOFORM
from app.models import TODOMODEL
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOFORM()
        todo_list = TODOMODEL.objects.filter(user=user).order_by('priority')
        context = {
            'form': form,
            'todo_list': todo_list
        }

        return render(request,'pages/home.html',context)

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request,'pages/login.html',context)

    else:
        form = AuthenticationForm(data=request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                Userlogin(request,user)
                return redirect('home')

        else:
            return render(request,'pages/login.html',context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
            }
        return render(request,'pages/signup.html',context)

    else:
       
        form = UserCreationForm(request.POST)
        context = {
            'form': form
            }
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'pages/signup.html',context)

def signout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        if request.method == 'POST':
            form = TODOFORM(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()

                print(form.cleaned_data)
                return redirect('home')
        else:
            context ={
                'form': form
            }
            return render(request,'pages/login.html',context)
    
def delete_todo(request , id):
    todo_list = TODOMODEL.objects.get(pk=id).delete()
    return redirect('home')

def Change_status(request,id ,status):
    todo_list = TODOMODEL.objects.get(pk=id)
    todo_list.status = status
    todo_list.save()
    return redirect('home')


    
