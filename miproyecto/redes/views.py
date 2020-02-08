from django.shortcuts import render
from redes.forms import UserForm #,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def index(request):
    return render(request,'redes/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    #return index(request)
    #return redirect("https://doggos.ml")
    #return redirect('www.doggos.ml')

def redirect_login(request):
    response = redirect("/redes/user_login/")
    return response

@login_required
def redirect_to_app(request):
    response = redirect("/redes/perritos/")
    return response

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid(): # and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #if 'profile_pic' in request.FILES:
            #    print('found it')
            #    profile.profile_pic = request.FILES['profile_pic']
            #profile.save()
            registered = True
            #return redirect_login(request)
            return HttpResponseRedirect(reverse('redes:user_login'))
        else:
            print(user_form.errors) #,profile_form.errors)
    else:
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()
    return render(request,'redes/registration.html',
                          {'user_form':user_form,
                           #'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('redes:perritos'))
                #return redirect_to_app(request)
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'redes/login.html', {})

def perritos(request):
    current_user = request.user
    if current_user.is_authenticated:
        #return HttpResponseRedirect(reverse('redes:perritos'))
        #return redirect('redes:perritos')
        return render(request, 'redes/perritos.html', {})
        #return render(request, 'redes/index.html', {})
        #index(request)
    else:
        #return redirect('user_login')
        #return HttpResponseRedirect(reverse('user_login'))
        return render(request, 'redes/login.html', {})
