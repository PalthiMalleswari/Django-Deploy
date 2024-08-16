from django.shortcuts import render
from django.http import HttpResponse,request,HttpResponseRedirect
from .models import Topic,Webpage,AccessRecord
from . import forms
from .forms import UserForm,UserProfileInfoForm


from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required





# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, World !</h1>")

def index(request):
    # name = {'name' : 'Stupid'}
    # return render(request,'Card-Game.html',name)
    return render(request,'index.html')

def listing_topics(request):
    topics = Topic.objects.all()
    name = {'name':'Malli','age':21}
    data = {'topics':topics,'details':name}
    print(topics)


    return render(request,'display.html',data)

def login_check(request):
    form = forms.loginForm()
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            print("Validation successfull !")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request,'loginForm.html',{'form':form})

def usersform(request):

    form = forms.NewUserForm()

    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM Invalid')
    
    return render(request,'users.html',{'form':form})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'registration.html',
                  {'user_form': user_form,
                   'profile_form':profile_form,
                   'registered':registered})




def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                return HttpResponse("Account Not Activate")
            
        else:
            print("Someone tried to login and failed !")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("Invali Login details supplied !")
        
    else:
        return render(request,'login.html',{})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice !")
