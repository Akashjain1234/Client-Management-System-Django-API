from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from myapp.form import *
from myapp.models import *
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def home_page(request):
    api_urls = {
        'Add Client': 'add/',
        'Display Client': 'display/',
        'Update Client': 'update/<int:id>/',
        'Delete Client': 'delete/<int:id>/',
        'Display Project': 'displaypro/',
        'Display Client Info': 'clientinfo/<int:id>/',
        'Login': 'login/',
        'Logout': 'logout/',
        'Signup': 'signup/',
        }
    return Response(api_urls)

@api_view(['POST'])
def add_page(request):
    serializer = ClientForm(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def display_page(request):
    data = Client.objects.all()
    serializer = Clientserializer(data, many=True)
    return Response(serializer.data)
   

@api_view(['POST'])
def update_page(request,id):
    s1 = Client.objects.get(id=id)
    serializer = Clientserializer(instance=s1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
   

@api_view(['DELETE'])
def delete_page(request,id):
    s1 = Client.objects.get(id=id)
    s1.delete()
    return Response('Item Deleted Successfully')


@api_view(['POST'])
def project_page(request,id):
    user = User.objects.all()
    client = Client.objects.get(id=id)
    serializer = Projectserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def displaypro_page(request):
    data = Project.objects.all()
    serializer = Projectserializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Signup_page(request):
    serializer = SignupForm(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        form = SignupForm()
        serializer = Userserializer(form, many=True)
        return Response(serializer.data)
    

def login_page(request):
    serializer = SignupForm(data=request.data)
    if serializer== None:
        messages.info(request,'Please Enter Correct Username or Password....! ')
        return Response(messages)
    elif serializer.user.is_authenticated:
        return Response(serializer.data)

@api_view(['GET'])
def clientinfo_page(request,id):
    s1 = Client.objects.get(id=id)
    s2 = Project.objects.filter(client__name__exact=s1.name)
    serializer = Projectserializer(s2,s1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def delsuccess_page(request):
    return render (request,"myapp/delsuccess.html")

@api_view(['DELETE'])
def deletepro_page(request,id):
    s1 = Project.objects.get(id=id)
    s1.delete()
    return Response('Item Deleted Successfully')
    
    
    


