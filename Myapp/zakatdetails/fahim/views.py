from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Madrasadetails,Zakatdetails
from .forms import zakatentry,madrasaregisteration
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,email = email, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):


    
    # Render the template with the context
 return render(request, 'home.html')


"""def register(request): 
    # return response 
    return render(request, "register.html") """

def register(request):
     if request.method == 'POST':
        form = madrasaregisteration(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Data successfully inserted!")
     else:
        form = madrasaregisteration()
     return render(request, 'process_Madrasadetails.html', {'form': form})


def madrasa(request):
   details = Madrasadetails.objects.all().values()
   template = loader.get_template('madrasa.html')
   context = {
    'details': details,
   } 
   return HttpResponse(template.render(context, request))

@login_required
def madrasadetails(request, id):
    # Fetch the specific Madrasadetails instance or return a 404 error if not found
    details = get_object_or_404(Madrasadetails, id=id)
    
    user = request.user
    
    zakat_entries = Zakatdetails.objects.filter(madrasa_name=details,user_name=user)

    
    
  
    context = {
        'details': details,
        'zakat_entries': zakat_entries,
    }
    
    # Render the template with the context
    return render(request, 'madrasadetails.html', context)


def process_zakat_entry(request):
    if request.method == 'POST':
        form = zakatentry(request.POST)
        if form.is_valid():
         zakatdetails = form.save(commit=False)
         zakatdetails.user_name = request.user
         form.save()
        return HttpResponse("Data successfully inserted!")
    else:
        form = zakatentry()
    return render(request, 'zakat_entry.html', {'form': form})


