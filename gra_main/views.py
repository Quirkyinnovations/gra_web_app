from django.shortcuts import render, HttpResponse,redirect
from gra_news.models import News, SportNews
from .forms import RegistrationForm, RegistrationModelForm
from .models import Registration
from django.contrib import messages


# Create your views here.

def home(request):
    # return HttpResponse("<h1>We welcome you to glory restoration assembly GRA</h1>")
    # retrieve data from the database
    obj = News.objects.get(id=1)
    
    context = {
        "data":obj
    }
    
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,"aboutus.html")

def branches(request):
    return render(request,"branches.html")
    
def mission(request):
   return render(request,"mission.html")
    
def department(request):
    return render(request,"department.html")
    
def events(request, year):
    article_list = News.objects.filter(pub_date__year=year)
    
    context = {
        'year':year,
        'article_list': article_list
    }
    return render(request,"events.html",context)
    
def media(request):
    return render(request,"media.html")
    
def channel(request):
    return render(request,"channel.html")
    
def contactus(request):
    return render(request,"contactus.html")
    
def sermons(request):
    return render(request,"sermons.html")
    
def shop(request):
    return render(request,"shop.html")
    
def music(request):
    return render(request,"music.html")
    
def login(request):
    return render(request,"login.html")
    
def register(request):
    
    context = {
        "form":RegistrationForm
    }
    return render(request,"register.html",context)
    
def addUser(request):
    form = RegistrationForm(request.POST)
    
    # check if the form is valid
    if form.is_valid():
        myregister = Registration(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone'],
            password = form.cleaned_data['password'],
            location = form.cleaned_data['location']
        )
        # save data
        myregister.save()
        # show flash messages
        messages.add_message(request, messages.SUCCESS, "You have Signed Successfuly!")
        
    return redirect('register')
    
def modelForm(request):
    context = {
        'modelForm': RegistrationModelForm
    }
    return render(request, "modelForm.html", context)
    
def addModelForm (request):
    
    myModelForm = RegistrationModelForm(request.POST)
    
    if myModelForm.is_valid():
        myModelForm.save()
        messages.add_message(request, messages.SUCCESS, "Save Successfuly")
        
    return redirect('modelForm')
        