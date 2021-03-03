from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# @login_required(login_url='login')
def index(request):
    if request.session['user']:
        return redirect('home')

    return render(request,'index.html')

def home(request):
    user = request.session['user']
    user = Person.objects.filter(username = user).first()
    entries = Entry.objects.filter(person=user).order_by('-date_posted')
    context = {
        'entries': entries
    }

    return render(request,'index.html',context) 

# @login_required(login_url='login')
def add(request,user_name):
    if user_name != request.session['user']:
        return HttpResponse("<h1>Page not available!<h1>")


    if request.method == 'POST':
        text = request.POST['text']

        user_obj = Person.objects.filter(username= user_name).first()
        upload_entry = Entry(person = user_obj,text = text)
        upload_entry.save()
        messages.success(request, 'Your Note has been uploaded successfully.')
        return redirect('home')

    return render(request,'add.html')    


def edit(request, pk):
    entry = Entry.objects.get(id=pk)
    form = EntryForm(instance= entry)
    context = {
        'entry': entry, 'form': form
    }
    if entry.person.username != request.session['user']:
        return HttpResponse("<h1>Page not available!<h1>")

    if request.method == 'POST':
        # text = request.POST['text']

        edit_entry = EntryForm(request.POST, instance=entry)
        edit_entry.save()
        messages.success(request, 'Your Note has been edited successfully.')
        return redirect('home')

    return render(request, 'edit.html', context)    


def delete(request,pk):
    model = Entry
    delete_entry = Entry.objects.get(id=pk)

    if delete_entry.person.username != request.session['user']:
        return HttpResponse("<h1>Page not available!<h1>")

    if request.method == 'POST':
        delete_entry.delete()
        return redirect('home')
        messages.success(request, 'Your post has been deleted successfully.')

    context = {
        'item': delete_entry
    }    

    return render(request,'delete.html', context)

       


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            request.session['user'] = username
            return redirect('home')
        else:
            messages.info(request, "Username or Password is Invalid")   
    context = {}
    return render(request, 'login.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            Person.objects.create(
                user = user,
                username = user.username,
                email = user.email
            )


            messages.success(request, "Account was created for "+ username)
            form = CreateUserForm()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)  



def LogoutUser(request):
    try:
        del request.session['user']
    except:
        return redirect('login')    
    return redirect('login')



def custom_page_not_found_view(request,exception):
    return render(request, '404.html', {})


def custom_error_view(request,exception=None):
    return render(request, '500.html', {})

def custom_permission_denied_view(request,exception=None):
    return render(request, '403.html', {})

def custom_bad_request_view(request,exception=None):
    return render(request, '400.html', {})