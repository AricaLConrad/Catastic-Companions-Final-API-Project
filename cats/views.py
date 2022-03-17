# Sources I Used:
# https://www.codegrepper.com/search.php?q=how%20to%20create%20staff%20account%20in%20django?
# https://openclassrooms.com/en/courses/7107341-intermediate-django/7265147-assign-permissions-using-groups?msclkid=bd0a39bfa57611eca03d343850bc9fc4
# https://pythonguides.com/login-system-in-python-django/
# https://stackoverflow.com/questions/29279893/how-to-redirect-my-own-login-to-admin-login-in-django

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group, Permission

from rest_framework import generics

from .models import Cat
from .serializers import CatSerializer


class ListCat(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class DetailCat(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

def signup(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username = username).exists():

                messages.info(request, 'This username already exists. Please choose a different one.')
                return redirect(signup)
            
            elif User.objects.filter(email = email).exists():

                messages.info(request, 'This email has already been used. Please use a different one.')
                return redirect(signup)
            
            else:

                user = User.objects.create_user(email = email, username = username, password = password)
                user.is_staff = True
                permissionone = Permission.objects.get(codename = 'add_cat')
                permissiontwo = Permission.objects.get(codename = 'change_cat')
                permissionthree = Permission.objects.get(codename = 'delete_cat')
                permissionfour = Permission.objects.get(codename = 'view_cat')
                user.user_permissions.add(permissionone)
                user.user_permissions.add(permissiontwo)
                user.user_permissions.add(permissionthree)
                user.user_permissions.add(permissionfour)
                user.save()
                return redirect('login')

        else:

            messages.info(request, 'These passwords do not match.')
            return redirect(signup)
        
    else:

        return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password. Please check if they are typed correctly.')
            return redirect('login')

    else:
        return render(request, 'login.html')

def home(request):

    return render(request, 'home.html')

def logout(request):

    auth.logout(request)
    return redirect('home')