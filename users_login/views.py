from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_handler(request):
    if request.POST and 'only for login.html' in request.POST:
        email=request.POST['email']
        pass1=request.POST['pass']
        user=authenticate(request=request,username=email,password=pass1)
        if user is not None:
            login(request,user)
            print('logged in ')
            if 'next' in request.POST:
                next=request.POST['next']
                print('next=',next)
                return redirect(next)
            return redirect('/home')
        else:
            return render(request,'login.html',{'error':'invalid user or password'})
    else:
        return render(request,'login.html')
        
def signup_handler(request):
    if request.POST:
        username=request.POST['user_name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        user=User.objects.create_user(username,email,pass1)
        user.save()
        return redirect('/validate/login')
    else:
        return render(request,'signup.html',{'user_name':'','email':''})

def logout_handler(request):
    logout(request)
    return redirect('/')

def forgot_password(requset):
    pass

    