from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect ('account/'+username)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def account (request,uname):
   
    return render(request, 'account.html',{'usern':uname})

def logout(request):
    auth.logout(request)
    return redirect ("/")

def check(request):
    username = request.POST.get('query')
    if User.objects.filter(username=username).exists():
        
    
        return redirect('search/'+username)
    else:
        username = 'User not found'
        return redirect('search/'+username)

def search(request,user):
    if User.objects.filter(username=user).exists():
        uname = User.objects.get(username=user)
        name = uname.username
        email = uname.email
       
        details = {'name':name, 'email':email}
        return render(request, 'search.html',details)
    else: 
        return render(request, 'search.html',{'user':user})
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        if password1 == password2:
            if User.objects.filter (username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else: 
                user = User.objects.create_user(username=username, password=password1,email=email)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def update(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        details = {'username':username, 'password':password, 'email':email}
        return render(request, 'update.html',details)

def changeup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm_password')
    email = request.POST.get('email')
    user = User.objects.get(username=username)
    user.email = email

    if password == '' or confirm == '':
        # If password fields are empty, keep the current password
        pass
    elif password != confirm:
        messages.info(request, 'Password not matching')
        return redirect('update')
    elif password == confirm:
        user.set_password(password)  # Use set_password method
        user.email = email
        user.save()
   
    user.save()
    return redirect('login')